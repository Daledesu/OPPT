#from django.urls import resolve
#from django.test import TestCase
#from schedulePT.views import MainPage
#from django.http import HttpRequest
#from django.template.loader import render_to_string
#from django.urls import resolve
#from django.urls import render
#from django.urls import response
#from schedulePT.models import StudentInfo

#class HomePageTest(TestCase):

	"""def test_mainpage_as_seen_client(self):
		resp = self.client.get('/')
		self.assertTemplateUsed(resp, 'mainpage.html')"""
	
	"""def test_responding_post_request(self):
		resp = self.client.post('/', data={'studentName' :'NameNew'})
		self.assertIn('NameNew', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'FstudentName' :'FNameNew'})
		self.assertIn('FNameNew', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'LstudentName' :'LNameNew'})
		self.assertIn('LNameNew', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'MstudentName' :'MNameNew'})
		self.assertIn('MNameNew', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')"""

	"""hiwalay ng progress"""

	"""def test_mainpage_bilang_silent(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'mainpage.html')
	
	def test_isave_yung_POST_request(self):
		response = self.client.post('/',data={'studentName' :'NameNew',
											'FstudentName' :'FNameNew', 
											'LstudentName' :'LNameNew', 
											'MstudentName' :'MNameNew'})
		self.assertEqual(StudentInfo.objects.count(), 1)
		newEntry = StudentInfo.objects.first()
		
		self.assertEqual(newEntry.studentName, 'NameNew')

	def test_iredirect_yung_POST(self):
		response = self.client.post('/',data={'studentName' :'NameNew',
											'FstudentName' :'FNameNew', 
											'LstudentName' :'LNameNew', 
											'MstudentName' :'MNameNew'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_kapag_magsave_lang_necessary(self):
		self.client.get('/')
		self.assertEqual(StudentInfo.objects.count(), 0)

class ORMTest(TestCase):
	def test_saving_kapag_magretrieve_ng_list(self):
		entry1 = StudentInfo()
		entry1.studentName = 'Dale'
		entry1.FstudentName = 'Jean'
		entry1.LstudentName = 'Maliksi'
		entry1.MstudentName = 'Carlet'
		entry1.save()

		entry2 = StudentInfo()
		entry2.studentName = 'Lucia'
		entry2.FstudentName = 'Liv'
		entry2.LstudentName = 'Lee'
		entry2.MstudentName = 'Kamui'
		entry2.save()

		items = StudentInfo.objects.all()

		self.assertEqual(items.count(), 2)
		items1 = items[0]
		items2 = items[1]
		self.assertEqual(items1.studentName, 'Dale')
		self.assertEqual(items2.studentName, 'Lucia')

	def test_template_if_mag_display_list_na(self):
		StudentInfo.objects.create(FstudentName='Jean')
		StudentInfo.objects.create(FstudentName='Liv')
		response = self.client.get('/')
		self.assertIn('Jean', response.content.decode())
		self.assertIn('Liv', response.content.decode())"""