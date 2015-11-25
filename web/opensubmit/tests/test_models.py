'''
    Test cases for specific model functions that are difficult to test in larger context.
'''

from opensubmit.tests.cases import StudentTestCase, SubmitTutorTestCase, SubmitAdminTestCase

class AssignmentModelStudentTestCase(StudentTestCase):
    def setUp(self):
        super(AssignmentModelStudentTestCase, self).setUp()

class AssignmentModelTutorTestCase(SubmitTutorTestCase):
    def setUp(self):
        super(AssignmentModelTutorTestCase, self).setUp()

    def testScriptUrl(self):
    	self.assertIsNone(self.openAssignment.validity_test_url())
    	self.assertIsNotNone(self.validatedAssignment.validity_test_url())
    	self.assertIsNone(self.softDeadlinePassedAssignment.validity_test_url())
    	self.assertIsNone(self.hardDeadlinePassedAssignment.validity_test_url())
    	self.assertIsNone(self.unpublishedAssignment.validity_test_url())

class AssignmentModelAdminTestCase(SubmitAdminTestCase):
    def setUp(self):
        super(AssignmentModelAdminTestCase, self).setUp()

    def testScriptUrl(self):
    	self.assertIsNone(self.openAssignment.validity_test_url())
    	self.assertIsNotNone(self.validatedAssignment.validity_test_url())
    	self.assertIsNone(self.softDeadlinePassedAssignment.validity_test_url())
    	self.assertIsNone(self.hardDeadlinePassedAssignment.validity_test_url())
    	self.assertIsNone(self.unpublishedAssignment.validity_test_url())



