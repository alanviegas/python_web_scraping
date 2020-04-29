import logging
import requests
import json
from datetime import datetime

from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults
from airflow.operators.sensors import BaseSensorOperator
from airflow.operators.http_operator import SimpleHttpOperator

log = logging.getLogger(__name__)

class MyFirstSensor(BaseSensorOperator):

    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(MyFirstSensor, self).__init__(*args, **kwargs)

    def poke(self, context):
        current_minute = datetime.now().minute
        if current_minute % 3 != 0:
            log.info("Current minute (%s) not is divisible by 3, sensor will retry.", current_minute)
            return False

        log.info("Current minute (%s) is divisible by 3, sensor finishing.", current_minute)
        task_instance = context['task_instance']
        task_instance.xcom_push('sensors_minute', current_minute)
        return True

class MyFirstOperator(BaseOperator):

    @apply_defaults
    def __init__(self, my_operator_param, *args, **kwargs):
        self.operator_param = my_operator_param
        super(MyFirstOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info("Hello World!")
        log.info('operator_param: %s', self.operator_param)
        task_instance = context['task_instance']
        sensors_minute = task_instance.xcom_pull('my_sensor_task', key='sensors_minute')
        log.info('Valid minute as determined by sensor: %s', sensors_minute)


class GetReclameAqui(BaseOperator):

    @apply_defaults
    def __init__(self, company, collection, *args, **kwargs):
        super(GetReclameAqui, self).__init__(*args, **kwargs)
        self.params = {}
        self.params['company'] = company
        self.collection = collection
        self.url = 'http://api_consultareclameaqui:5000/{}'.format(self.collection)
    
    def execute(self, context):
        log.debug('GetReclameAqui url: {}'.format(self.url)) 
        log.debug('GetReclameAqui params: {}'.format(self.params))
 
        response = requests.get(self.url, params=self.params)
        #response_fmt = {response.status_code : response.text}
        response_fmt = response.text
        log.debug('GetReclameAqui response: {}'.format(response_fmt))
 
        task_instance = context['task_instance']
        task_instance.xcom_push('response', response_fmt)
   

class PersisteDatabase(BaseOperator):

    @apply_defaults
    def __init__(self, method, company, collection, date='', *args, **kwargs):
        super(PersisteDatabase, self).__init__(*args, **kwargs)
        self.method = method
        self.params = {}
        self.params['company'] = company
        self.date = date
        self.collection = collection
   
        if (self.date == ''):
            self.params['date'] = datetime.today().strftime('%Y%m%d')
        self.url = 'http://api_persistenciadados:5005/{}/'.format(self.collection)
 
    def execute(self, context):
        if self.method == 'POST':
            log.debug('PersisteDatabase params: {}'.format(self.params))

            task_instance = context['task_instance']
            jsondata = task_instance.xcom_pull('consulta_reclameaqui', key='response')
            log.debug('PersisteDatabase jsondata: {}'.format(jsondata))

            response = self.__post_data(jsondata)
            log.debug('PersisteDatabase response: {}, {}'.format(response.status_code, response.text))

        elif self.method == 'GET':
            log.debug('PersisteDatabase params: {}'.format(self.params))
            response = self.__get_data()
            response_fmt = response.text
            log.debug('PersisteDatabase response: {}'.format(response_fmt))
            
            task_instance = context['task_instance']
            task_instance.xcom_push('response', response_fmt)

        elif method == 'DELETE':
            log.debug('PersisteDatabase params: {}'.format(self.params))
            response = self.__delete_data()

    def __post_data(self, jsondata):
        headers = {'content-type': 'application/json'}
        data = jsondata
        return requests.post(self.url, params=self.params, data=data, headers=headers)
    
    def __get_data(self):
        return requests.get(self.url, params=self.params)

    def __delete_data(self):
        return requests.delete(self.url, params=self.params)


class MyFirstPlugin(AirflowPlugin):
    
    name = "my_first_plugin"
    operators = [MyFirstOperator, MyFirstSensor, GetReclameAqui, PersisteDatabase]


