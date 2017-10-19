import sys, os, unittest, importlib

script, start_directory = sys.argv
tests = []

class TestObj:

	def __init__(self, name):
		print("A TestObj with '{0}' name was initiated".format(name))
		self.name = name
		self.module = None

		self.task_name = name.replace('test_', '')
		self.task_modules_names = []
		
		self.test_suit = self.results = None

	def __search_task_modules(self):
		for root, dirs, files in os.walk(start_directory):
			for file in files:
				if (not file.startswith('test_')) and self.task_name in file and file.endswith('.py'):
					if root not in sys.path:
						sys.path.append(root)
					self.task_modules_names.append(file[:-3])

	def __runTests(self):
		for name in self.task_modules_names:
			print("A task with '{0}' name is in test".format(name))
			task_module = importlib.import_module(name)
			self.test_suit = unittest.defaultTestLoader.loadTestsFromModule(self.module)
			runner = unittest.TextTestRunner()
			func_name = self.module.func_to_test
			setattr(self.module, func_name, getattr(task_module, func_name))

			self.result = runner.run(self.test_suit)

			setattr(self.module, func_name, lambda: None)
			del task_module
			del sys.modules[name]

	def run(self):
		self.__search_task_modules()
		self.__runTests()



def search_test_modules():
	for root, dirs, files in os.walk(start_directory):
		for file in files:
			if file.startswith('test_') and file.endswith('.py'):
				test = TestObj(file[:-3])
				tests.append(test)
				if root not in sys.path:
					sys.path.append(root)
				test.module = importlib.import_module(test.name)


search_test_modules()
for test in tests:
	test.run()