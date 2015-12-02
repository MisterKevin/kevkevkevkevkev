from flask import render_template, request
from app import app
from schedule_api import *

@app.route('/')
def index():
    options = {}

    options['terms'] = get_terms()

    return render_template('index.html', **options)

@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/<test>')
def test2(test):
	return render_template('test.html')

@app.route('/term=<int:termCode>')
def getSchools(termCode):
	options = {}

	options['termCode'] = termCode
	options['schools'] = get_schools(termCode)

	return render_template('schools.html', **options)

@app.route('/term=<int:termCode>/school=<school>')
def getSubjects(termCode, school):
	options = {}
	options['termCode'] = termCode
	options['schoolCode'] = school
	options['subjects'] = get_subjects(termCode, school)

	return render_template('subjects.html', **options)

@app.route('/term=<int:termCode>/school=<school>/subject=<subject>')
def getCatalogNumbers(termCode, school, subject):
	options = {}

	options['termCode'] = termCode
	options['schoolCode'] = school
	options['subjectCode'] = subject
	options['catalog'] = get_catalog_numbers(termCode, school, subject)

	return render_template('catalog.html', **options)

@app.route('/term=<int:termCode>/school=<school>/subject=<subject>/catalog=<int:catalog>')
def getCourseDescription(termCode, school, subject, catalog):
	options = {}
	options['sectionDetails'] = {}
	options['instructorDetails'] = {}

	options['sectionNums'] = get_section_nums(termCode, school, subject, catalog)
	options['courseDescr'] = get_course_description(termCode, school, subject, catalog)

	for obj in options['sectionNums']:
		options['sectionDetails'][obj] = get_section_details(termCode, school, subject, catalog, obj)
		options['instructorDetails'][obj] = get_meetings(termCode, school, subject, catalog, obj)

	return render_template('courses.html', **options)

