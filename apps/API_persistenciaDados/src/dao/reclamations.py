#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date: 20200316
User: Alan Viegas
Project: Search on site ReclameAqui.com.br for score-points and reclamations of the Company

R0: Initial version

"""
import sys

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.firefox.options import Options, Log 
from time import sleep
from utils.paths import get_project_root, get_url

class CompanyReclamations:

    def __init__(self):
        self._base_url = get_url()
        
        #self._firefox_log = Log()
        self._firefox_options = Options()
        self._firefox_options.headless = True
        
        #self._firefox_options.add_argument(self._firefox_log)
        #caminho = '{}/log/geckodriver.log'.format(get_project_root())
        #print ("debugando")
        #print(caminho)

        self._firefox = webdriver.Firefox(options = self._firefox_options,
                                          executable_path = r'{}/utils/geckodriver'.format(get_project_root()),
                                          log_path= r'{}/log/geckodriver.log'.format(get_project_root())
                                          )
        self._firefox.get(self._base_url)
        sleep(2)

    def search_company(self, company_name):
        self._company_name = company_name
        self._firefox.find_element_by_class_name('input-auto-complete-search').send_keys(self._company_name)
        sleep(2)

        for company in self._firefox.find_elements_by_class_name('card-company'):
            if company.find_element_by_class_name('company-name').text == self._company_name:
                self._company_link = company.find_element_by_class_name('company-name')
                break

        self._company_link.click()
        sleep(2)

        self._firefox.find_element_by_class_name('menu-item').click()
        sleep(2)

    def close(self):
        self._firefox.quit()

    @property
    def get_scores(self):
        self._bs_obj = bs(self._firefox.page_source, 'html.parser')
        self._scores_draft = self._bs_obj.findAll('span', {'class': 'company-index-label-value ng-binding'})

        self._scores_values = [score.getText() for score in self._scores_draft]
        self._scores_keys = ['reclamations', 'answered', 'unanswered', 'response_time']
        self._scores = dict(zip(self._scores_keys, self._scores_values))

        return self._scores

    @property
    def get_reclamations(self):
        self._bs_obj = bs(self._firefox.page_source, 'html.parser')

        # get first 10 reclamations
        self._boxes = self._bs_obj.find_all('a', { 'class': 'link-complain-id-complains label-not-answered'})
        #self._boxes = self._bs_obj.find_all('li',
        #                                    {'ng-repeat': 'complain in vm.complainList.data track by $index | limitTo:10'})

        #self._href_links = [box.find('a').get('href') for box in self._boxes]
        self._href_links = [box.get('href') for box in self._boxes]
        self._page_links = [self._base_url + link for link in self._href_links]
        
        self._first_10_reclam = {}
        for idx, reclamation_link in enumerate(self._page_links):
            
            #print('DEBUG: {}'.format(reclamation_link))
            self._firefox.get(reclamation_link)
            sleep(2)

            self._bs_page = bs(self._firefox.page_source, 'html.parser')
            self._title = self._bs_page.find('h1', {'class': 'ng-binding'}).text
            self._title = self._title.strip(' ')

            self._locale_date = self._bs_page.find('ul', {'class': 'local-date list-inline'}).text
            self._locale_date = self._locale_date.replace('denunciar', '').strip(' ')

            self._description = self._bs_page.find('div', {'class': 'complain-body'}).text
            self._description = self._description.strip(' ')

            self._first_10_reclam[idx] = {'title': self._title,
                                          'locale_date': self._locale_date,
                                          'description': self._description}
        return self._first_10_reclam
