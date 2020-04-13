"""
Date: 20200316
User: Alan Viegas
Project: Search on site ReclameAqui.com.br for score-points and reclamations of the Company

"""
import pytest
from unittest import TestCase
from src.dao.reclamations import CompanyReclamations

class TestDao(TestCase):
    """
    Test for class on Dao layer
    """
    def test_get_scores(self):
        """
        :assert: Verify
        """
        cr = CompanyReclamations()
        cr.search_company('Cielo')
        scores = cr.get_scores

        answered = "5914"
        reclamations = "6160"
        response_time = "14 dias e 8 horas "
        unanswered = "246"

        assert (answered == scores["answered"])
        assert (reclamations == scores["reclamations"])
        assert (response_time == scores["response_time"])
        assert (unanswered == scores["unanswered"])

#if __name__ == '__main__':
#    TestDao().test_get_scores()


'''
reclamations = cr.get_reclamations
print(reclamations)
cr.close()
'''
