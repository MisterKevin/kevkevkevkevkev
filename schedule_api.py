import json
import time
import requests

class ScheduleApiError(Exception):
	'''
	Raised if there is an error with the schedule API.
	'''
	pass

# The base API endpoint
base_url = 'http://umich-schedule-api.herokuapp.com'

# the amount of time to wait for the schedule API
timeout_duration = 25


def get_data(relative_path):
	'''
	Gets data from the schedule API at the specified path.
	Will raise a ScheduleApiError if unsuccessful.
	Assumes API will return JSON, returns as a dictionary.
	'''

	timeout_at = time.time() + timeout_duration

	while time.time() < timeout_at:
		r = requests.get(base_url + relative_path)
		if r.status_code == 200:
			return json.loads(r.text)
		if r.status_code == 400:
			break

	raise ScheduleApiError('error for url: {0} message: "{1}" code: {2}' \
		.format(relative_path, r.text, r.status_code))

def get_terms():
	'''
	Returns a list of valid terms.
	Each item in the list is a dictionary containing:
		('TermCode', 'TermDescr', 'TermShortDescr')
	'''
	return get_data('/get_terms')

def get_schools(termCode):
	'''
	Gets the school
	'''

	var = '/get_schools'
	var = var + '?term_code=' + str(termCode)
	return get_data(var)

def get_subjects(termCode, school):
	'''
	Gets the subjects 
	'''
	var = '/get_subjects'
	var = var + '?term_code=' + str(termCode)
	var = var + '&school=' + school
	return get_data(var)

def get_catalog_numbers(termCode, school, subject):
	'''
	Gets the catalog numbers 
	'''
	var = '/get_catalog_numbers'
	var = var + '?term_code=' + str(termCode)
	var = var + '&school=' + school
	var = var + '&subject=' + subject

	return get_data(var)

def get_course_description(termCode, school, subject, catalogNum):
	'''
	Gets the course description 
	'''
	var = '/get_course_description'
	var = var + '?term_code=' + str(termCode)
	var = var + '&school=' + school 
	var = var + '&subject=' + subject 
	var = var + '&catalog_num=' + str(catalogNum)

	return get_data(var)

def get_section_nums(termCode, school, subject, catalogNum):
	'''
	Gets the section numbers 
	'''
	var = '/get_section_nums'
	var = var + '?term_code=' + str(termCode)
	var = var + '&school=' + school 
	var = var + '&subject=' + subject 
	var = var + '&catalog_num=' + str(catalogNum)

	return get_data(var)

def get_section_details(termCode, school, subject, catalogNum, sectionNum):
	'''
	Gets the section details 
	'''
	var = '/get_section_details'
	var = var + '?term_code=' + str(termCode)
	var = var + '&school=' + school 
	var = var + '&subject=' + subject 
	var = var + '&catalog_num=' + str(catalogNum)
	var = var + '&section_num=' + "{0:0>3}".format(str(sectionNum))

	return get_data(var)

def get_meetings(termCode, school, subject, catalogNum, sectionNum):
	'''
	Gets meeting details
	'''
	var = '/get_meetings'
	var = var + '?term_code=' + str(termCode)
	var = var + '&school=' + school 
	var = var + '&subject=' + subject 
	var = var + '&catalog_num=' + str(catalogNum)
	var = var + '&section_num=' + "{0:0>3}".format(str(sectionNum))

	return get_data(var)

def get_textbooks(termCode, school, subject, catalogNum, sectionNum):
	'''
	Gets textbook information
	'''
	var = '/get_textbooks'
	var = var + '?term_code=' + str(termCode)
	var = var + '&school=' + school 
	var = var + '&subject=' + subject 
	var = var + '&catalog_num=' + str(catalogNum)
	var = var + '&section_num=' + "{0:0>3}".format(str(sectionNum))
	
	return get_data(var)

def get_instructors(termCode, school, subject, catalogNum, sectionNum):
	'''
	Gets textbook information
	'''
	var = '/get_instructors'
	var = var + '?term_code=' + str(termCode)
	var = var + '&school=' + school 
	var = var + '&subject=' + subject 
	var = var + '&catalog_num=' + str(catalogNum)
	var = var + '&section_num=' + "{0:0>3}".format(str(sectionNum))
	
	return get_data(var)


