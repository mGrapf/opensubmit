The Submit project
==================

Peter Tröger <peter.troeger@hpi.uni-potsdam.de>

This is Submit, a small web application for managing student assignment solutions in a university environment.

Other tools, such as Moodle, are more powerful and support assignments, the management of learning material, course progress organization and access management at the same time. If you want the all-inclusive solution, this is the wrong project.

Submit offers a trivial web page were students can login and submit their assignment solutions. Teachers and their personal use the backend interface to manage the list of available assignments, deadlines, and the gradings. Students are informed about the progress of their correction and their final grade via eMail and the frontend page.

The unique capability of Submit is the support for coding assignments, were students upload their programming excercise solution as source code archive. Submit offers a separate executor daemon, which runs on another machine and downloads submitted solutions from the web server. These archives are unpacked and tested for compilation,  so that non-compiling assignment solutions are rejected by the system before the deadline. 
This makes the life of the corrector less miserable, because at the point of the assignment deadline, all gradable solutions are 'valid' (e.g. compile). Students also seem to like the idea of having a validated solution, so that they do not fail due to technical difficulties at the correctors side.

Since Submit is only for assignment submission, it has no management of course participants. Everbody who can perform a successful login can submit solutions. We expect you to have an institute-specific OpenID provider, otherwise you need to contributre your own patches.

Installation of the web application
-----------------------------------

- Download the source code distribution of the web application.
- Unpack it somehwere in a folder that your web server can access.
- Run "pip install -r requirements.txt".
- Copy settings.ini.template to /etc/submit/settings.ini and edit it according to your local needs. 
- Run "manage.py syncdb" and "manage.py migrate" to create / update the configured database. On creation,
  this will also establish an administrator account.
- Configure your web server to serve Submit as WSGI application. Typically, we would expect some snippet like this inside a VirtualHost definition:

	    WSGIScriptAlias /submit <src_dir>/submit/wsgi.py
    	WSGIDaemonProcess submit
    	WSGIProcessGroup  submit
    	Alias /submit/static/admin /usr/local/lib/python2.6/dist-packages/Django-1.4.2-py2.6.egg/django/contrib/admin/static/admin
    	Alias /submit/static       <src_dir>/submit/static

- Perform a login into the teacher backend. Create some teacher accounts with "staff status" and according roles. Student logins are created automatically by the OpenID login functionality.

Submit runs happily without code validation as simple assignment submission tool. 

Installation of code executor
------------------------------

- Download the source code distribution of the executor application.
- Choose a dedicated machine beside the web server. This will compile (and run) the student submissions.
- Install the script from '/jobexec' there.
- Think again. IT WILL RUN THE STUDENT SUBMISSIONS. Perform all neccessary security precautions, such as network isolation and limited local rights.
- Adjust executor.cfg according to your needs.
- Add executor.py to cron, so that it regulary asks the web server for fresh work.

Creating an assignment
----------------------
- Create a course.
- Create a grading scheme for your course.
- Create an assignment for a course and grading scheme.

Assignment types
================

Any assignment can be configured in different ways with repsect to the expected student submission:

(A) No solution attachment, only text notes:
--------------------------------------------
Assignment.has_attachment = False
Assignment.attachment_test_compile = False
Assignment.attachment_test_validity = False
Assignment.attachment_test_full = False

(B) Submission of non-testable attachment (e.g. PDF file):
----------------------------------------------------------
Assignment.has_attachment = True
Assignment.attachment_test_compile = False
Assignment.attachment_test_validity = False
Assignment.attachment_test_full = False

(C) Submission of testable attachment, only compilation:
----------------------------------------------------------
Assignment.has_attachment = True
Assignment.attachment_test_compile = True
Assignment.attachment_test_validity = False
Assignment.attachment_test_full = False

(D) Submission of testable attachment, compilation and validation script run:
------------------------------------------------------------------------------
Assignment.has_attachment = True
Assignment.attachment_test_compile = True
Assignment.attachment_test_validity = True
Assignment.attachment_test_full = False

(E) Submission of testable attachment, compilation, validation and full test script run:
-----------------------------------------------------------------------------------------
Assignment.has_attachment = True
Assignment.attachment_test_compile = True
Assignment.attachment_test_validity = True
Assignment.attachment_test_full = True

State Model (TODO)
==================
	() ----> RECEIVED
	RECEIVED ----> SUBMITTED
	SUBMITTED --(*2)--> WITHDRAWN
	SUBMITTED_TESTED --(*2)--> WITHDRAWN
	TEST_COMPILE_PENDING --(*1)--> WITHDRAWN
	TEST_COMPILE_FAILED --(*2)--> WITHDRAWN
	TEST_VALIDITY_PENDING --(*1)--> WITHDRAWN
	TEST_VALIDITY_FAILED --(*2)--> WITHDRAWN
	TEST_FULL_PENDING--(*1)--> WITHDRAWN
	TEST_FULL_FAILED --(*2)--> WITHDRAWN

*1: Only if test is not currently executed, which would demand remote killing of test runs
*2: Only if assignment deadline is not over

To be continued ...
