#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pass
"""

__authors__ = "deepcaps"
__contact__ = "deepcaps@outlook.com"
__version__ = "1.0"
__copyright__ = "deepcaps"
__date__ = "None"

# Import library
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import platform


class connection():
	"""
	pass
	"""
	def drivers():
		"""
		pass
		"""
		global driver
		if platform.system() == "Windows":   # If system is Windows
			options = Options()
			options.add_argument('--headless')
			options.add_argument('--disable-gpu')
			options.add_argument('--no-sandbox')

			driver = webdriver.Chrome(executable_path="chromedriver.exe")
			# driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
			print ("driver: windows")
		elif platform.system() == "Linux" or platform.system() == "Darwin":   # If system is Linux or MacOS
			options = Options()
			options.add_argument('--headless')
			options.add_argument('--no-sandbox')
			
			driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)
			print ("driver: linux / macOS")
		else:
			print ("An error has occurred: incompatible operating system")
			return False
		return True

	def login(username, password, link):
		"""
		pass
		"""
		try:
			driver.get(link)   # get link
		except:
			print ("An error has occurred: the link is down")   # connection speed problem or link error
			return False
		try:
			time.sleep(5)
			id_bar = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[5]/div[4]/div[2]/div[2]/div/div[1]/div[2]/div[1]/input")
			mdp_bar = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[5]/div[4]/div[2]/div[2]/div/div[1]/div[2]/div[2]/input")
			button = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[5]/div[4]/div[2]/div[3]/button")

			id_bar.send_keys(username)
			mdp_bar.send_keys(password)
			button.click()
		except:
			print ("An error has occurred: not login")
			return False
		return True

class get_elements():
	"""
	pass
	"""
	def student_moyenne(username, password, link):
		"""
		pass
		"""
		if connection.drivers():
			if connection.login(username, password, link):
				# Go to "Notes" page
				time.sleep(5)
				driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div/div[3]/div[1]/div[3]/ul/li[3]/div[1]").click()   # Notes categorie
				webdriver.ActionChains(driver).move_by_offset(0,0).perform()   # Change position (close contextuel menu)

				# Get moyenne
				time.sleep(5)
				moyenne = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/table/tbody/tr/td[1]/div/div/div[2]/div[1]/div[2]/div/div/div[1]/span/span")   # Span student moyenne

				return moyenne.text   # Return student moyenne

	def classroom_moyenne(username, password, link):
		"""
		pass
		"""
		if connection.drivers():
			if connection.login(username, password, link):
				# Go to "Notes" page
				time.sleep(5)
				driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div/div[3]/div[1]/div[3]/ul/li[3]/div[1]").click()   # Notes categorie
				webdriver.ActionChains(driver).move_by_offset(0,0).perform()   # Change position (close contextuel menu)

				# Get moyenne
				time.sleep(5)
				moyenne = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/table/tbody/tr/td[1]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/span/span")   # Span classrooom moyenne

				return moyenne.text   # Return classroom moyenne
	
	def matter_moyenne(username, password, link):
		"""
		pass
		"""
		matters = ["MATHEMATIQUES", "ANGLAIS LV1", "ESPAGNOL LV2", "ARTS PLASTIQUES", "SVT"]
		notes = {}
		if connection.drivers():
			if connection.login(username, password, link):
				# Go to "Notes" page
				time.sleep(5)
				driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div/div[3]/div[1]/div[3]/ul/li[3]/div[1]").click()   # Notes categorie
				webdriver.ActionChains(driver).move_by_offset(0,0).perform()   # Change position (close contextuel menu)

				i = 0
				try:
					while True:
						div = driver.find_element_by_xpath('//*[@id="GInterface.Instances[2].Instances[1]_1_' + str(i) +'_div"]/div/div/div/div[2]')   # Div matter name
						for element in matters:
							if div.text == element:
								note = driver.find_element_by_xpath('//*[@id="GInterface.Instances[2].Instances[1]_1_' + str(i) +'_div"]/div/div/div/div[1]')   # Div notes
								notes[element] = str(note.text)   # Add note to "notes"
						i = i + 1
				except:
					return notes   # Return notes 