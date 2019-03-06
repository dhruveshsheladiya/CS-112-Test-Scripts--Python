# Based on testing harness dated 2017-06-02.

# STUDENTS: TO USE:
# 
# The following command will test all test cases on your file:
# 
#   python3 <thisfile.py> <your_one_file.py>
# 
# 
# You can also limit the tester to only the functions you want tested.
# Just add as many functions as you want tested on to the command line at the end.
# Example: to only run tests associated with func1 and func2, run this command:
# 
#   python3 <thisfile.py> <your_one_file.py> func1 func2
# 
# You really don't need to read the file any further, except that when
# a specific test fails, you'll get a line number - and it's certainly
# worth looking at those areas for details on what's being checked. This would
# all be the indented block of code starting with "class AllTests".


# INSTRUCTOR: TO PREPARE:
#  - add test cases to class AllTests. The test case functions' names must
# be precise - to test a function named foobar, the test must be named "test_foobar_#"
# where # may be any digits at the end, such as "test_foobar_13".
# - any extra-credit tests must be named "test_extra_credit_foobar_#"
# 
# - name all required definitions in REQUIRED_DEFNS, and all extra credit functions
#   in EXTRA_CREDIT_DEFNS. Do not include any unofficial helper functions. If you want
#   to make helper definitions to use while testing, those can also be added there for
#   clarity.
# 
# - to run on either a single file or all .py files in a folder (recursively):
#   python3 <thisfile.py> <your_one_file.py>
#   python3 <thisfile.py> <dir_of_files>
#   python3 <thisfile.py> .                    # current directory
# 
# A work in progress by Mark Snyder, Oct. 2015.
#  Edited by Yutao Zhong, Spring 2016.
#  Edited by Raven Russell, Spring 2017.
#  Edited by Mark Snyder, June 2017.


import unittest
import shutil
import sys
import os
import time


############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond 
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.
	
REQUIRED_DEFNS = ["exemption",
                  "credit",
                  "bracket_income",
                  "max_bracket",
                  "bracket_tax_rate",
                  "tax_withheld",
                  "tax_balance"
                  ]

# for method names in classes that will be tested
SUB_DEFNS = []

# definitions that are used for extra credit
EXTRA_CREDIT_DEFNS = []

# how many points are test cases worth?
weight_required = 1
weight_extra_credit = 0

# don't count extra credit; usually 100% if this is graded entirely by tests.
# it's up to you the instructor to do the math and add this up!
# TODO: auto-calculate this based on all possible tests.
total_points_from_tests = 85

# how many seconds to wait between batch-mode gradings? 
# ideally we could enforce python to wait to open or import
# files when the system is ready but we've got a communication
# gap going on.
DELAY_OF_SHAME = 1


# set it to true when you run batch mode... 
CURRENTLY_GRADING = False



# what temporary file name should be used for the student?
# This can't be changed without hardcoding imports below, sorry.
# That's kind of the whole gimmick here that lets us import from
# the command-line argument without having to qualify the names.
RENAMED_FILE = "student"

# END SPECIALIZATION SECTION
############################################################################
############################################################################


# enter batch mode by giving a directory to work on as the only argument.
BATCH_MODE = len(sys.argv)==2 and (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))

# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):
		
	############################################################################

	# exemption tests - 20pts
	def test_exemption_1  (self):self.assertEqual(exemption(11500.67,1,1),3000)
	def test_exemption_2  (self):self.assertEqual(exemption(17230.18,1,3),7000)
	def test_exemption_3  (self):self.assertEqual(exemption(21701,2,2),6000)
	def test_exemption_4  (self):self.assertEqual(exemption(35666,2,4),10000)
	def test_exemption_5  (self):self.assertEqual(exemption(41000,3,3),5000)
	def test_exemption_6  (self):self.assertEqual(exemption(58900,3,4),7000)
	def test_exemption_7  (self):self.assertEqual(exemption(60987,1,1),3000)
	def test_exemption_8  (self):self.assertEqual(exemption(79999,1,5),10200)
	def test_exemption_9  (self):self.assertEqual(exemption(85000,2,5),11700)
	def test_exemption_10  (self):self.assertEqual(exemption(97125,3,2),3000)
	def test_exemption_11  (self):self.assertEqual(exemption(100000,3,5),8700)
	def test_exemption_12  (self):self.assertEqual(exemption(110785,1,2),4850)
	def test_exemption_13  (self):self.assertEqual(exemption(123455,1,5),9855)
	def test_exemption_14  (self):self.assertEqual(exemption(131050,2,10),16270)
	def test_exemption_15  (self):self.assertEqual(exemption(159770,3,2),2115)
	def test_exemption_16  (self):self.assertEqual(exemption(1000,2,4),1000)
	def test_exemption_17  (self):self.assertEqual(exemption(15999,3,15),15999)
	def test_exemption_18  (self):self.assertEqual(exemption(160760,1,11),14100)
	def test_exemption_19  (self):self.assertEqual(exemption(400000,2,12),16200)
	def test_exemption_20  (self):self.assertEqual(exemption(678500,3,13),14200)

	# credit tests - 20pts
	def test_credit_1  (self): self.assertEqual(credit(0,1,1,0), 0)
	def test_credit_2  (self): self.assertEqual(credit(545.15,1,2,100), 20)
	def test_credit_3  (self): self.assertEqual(credit(1087,1,3,60), 60)
	def test_credit_4  (self): self.assertEqual(credit(1777.77,1,4,300), 90)
	def test_credit_5  (self): self.assertEqual(credit(3913.76,1,7,500), 210)
	def test_credit_6  (self): self.assertEqual(credit(4799,3,2,450), 120)
	def test_credit_7  (self): self.assertEqual(credit(6605,3,3,150), 150)
	def test_credit_8  (self): self.assertEqual(credit(8210.67,3,4,780), 260)
	def test_credit_9  (self): self.assertEqual(credit(9999.99,3,7,1350), 320)
	def test_credit_10  (self): self.assertEqual(credit(10999.99,3,10, 2100), 380)
	def test_credit_11  (self): self.assertEqual(credit(11450,2,2,1100), 660)
	def test_credit_12  (self): self.assertEqual(credit(12465.08,2,3,700), 700)
	def test_credit_13  (self): self.assertEqual(credit(13987,2,4,840), 820)
	def test_credit_14  (self): self.assertEqual(credit(14500.98,2,5,2000), 900)
	def test_credit_15  (self): self.assertEqual(credit(15120,2,8, 3050), 1000)
	def test_credit_16  (self): self.assertEqual(credit(15893.00,2,7,1740), 1000)
	def test_credit_17  (self): self.assertEqual(credit(16000.99,1,1,100), 0)
	def test_credit_18  (self): self.assertEqual(credit(17000.01,2,2,200), 0)
	def test_credit_19  (self): self.assertEqual(credit(20999.99,3,3,300), 0)
	def test_credit_20  (self): self.assertEqual(credit(123000.56,1,4,400), 0)

	# bracket_income tests	 - 10pts
	def test_bracket_income_1  (self): self.assertEqual(bracket_income(67234,1,1), 10000.00)
	def test_bracket_income_2  (self): self.assertEqual(bracket_income(17500,2,2), 0)
	def test_bracket_income_3  (self): self.assertEqual(bracket_income(87999.99,3,3), 43999.99)
	def test_bracket_income_4  (self): self.assertEqual(bracket_income(80001,1,4), 1)
	def test_bracket_income_5  (self): self.assertEqual(bracket_income(620000,2,5), 310000)
	def test_bracket_income_6  (self): self.assertEqual(bracket_income(5700.45,3,1), 5700.45)
	def test_bracket_income_7  (self): self.assertEqual(bracket_income(113450,1,2), 30000)
	def test_bracket_income_8  (self): self.assertEqual(bracket_income(80000.01,2,3), 10000.01)
	def test_bracket_income_9  (self): self.assertEqual(bracket_income(290998,2,4), 130998)
	def test_bracket_income_10  (self): self.assertEqual(bracket_income(170000,3,5), 0)
     

	# max_bracket tests - 10pts
	def test_max_bracket_1  (self): self.assertEqual(max_bracket(100,3), 1)
	def test_max_bracket_2  (self): self.assertEqual(max_bracket(15678,1), 2)
	def test_max_bracket_3  (self): self.assertEqual(max_bracket(20000.00,2), 1)
	def test_max_bracket_4  (self): self.assertEqual(max_bracket(47890.99,3), 3)
	def test_max_bracket_5  (self): self.assertEqual(max_bracket(103560,2), 3)
	def test_max_bracket_6  (self): self.assertEqual(max_bracket(104560.67,1), 4)
	def test_max_bracket_7  (self): self.assertEqual(max_bracket(80000.00,1), 3)
	def test_max_bracket_8  (self): self.assertEqual(max_bracket(310000.00,2), 4)
	def test_max_bracket_9  (self): self.assertEqual(max_bracket(310000.01,2), 5)
	def test_max_bracket_10  (self): self.assertEqual(max_bracket(170000.01,3), 5)
     

	# bracket_tax_rate tests - 5pts
	def test_bracket_tax_rate_1  (self): self.assertEqual(bracket_tax_rate(1,1), 0.1)
	def test_bracket_tax_rate_2  (self): self.assertEqual(bracket_tax_rate(2,2), 0.12)
	def test_bracket_tax_rate_3  (self): self.assertEqual(bracket_tax_rate(3,3), 0.24)
	def test_bracket_tax_rate_4  (self): self.assertEqual(bracket_tax_rate(2,4), 0.25)
	def test_bracket_tax_rate_5  (self): self.assertEqual(bracket_tax_rate(1,5), 0.32)
     

	# tax_withheld tests - 5pts
	def test_tax_withheld_1  (self): self.assertEqual(tax_withheld(0), 0)
	def test_tax_withheld_2  (self): self.assertEqual(tax_withheld(19878), 2753.6)
	def test_tax_withheld_3  (self): self.assertEqual(tax_withheld(64785), 8974.34)
	def test_tax_withheld_4  (self): self.assertEqual(tax_withheld(100015), 13854.61)
	def test_tax_withheld_5  (self): self.assertEqual(tax_withheld(183659), 25623.32)
     
	
	# tax_balance tests	
	def test_tax_balance_1  (self): self.assertEqual(tax_balance(15893.01,1,1), -854.42)
	def test_tax_balance_2  (self): self.assertEqual(tax_balance(13500,1,2), -1430.09)
	def test_tax_balance_3  (self): self.assertEqual(tax_balance(40000.01,1,4), -1985.0)
	def test_tax_balance_4  (self): self.assertEqual(tax_balance(160000,1,6), 7761.5)
	def test_tax_balance_5  (self): self.assertEqual(tax_balance(160001.01,1,14), 6681.6)
	def test_tax_balance_6  (self): self.assertEqual(tax_balance(15893,2,11), -2201.58)
	def test_tax_balance_7  (self): self.assertEqual(tax_balance(20000.99,2,2), -1370.54)
	def test_tax_balance_8  (self): self.assertEqual(tax_balance(125864,2,4), 1229.66)
	def test_tax_balance_9  (self): self.assertEqual(tax_balance(160000.10,2,20), 1299.51)
	def test_tax_balance_10  (self): self.assertEqual(tax_balance(311000,2,3), 21359.8)
	def test_tax_balance_11  (self): self.assertEqual(tax_balance(10,3,2), -1.39)
	def test_tax_balance_12  (self): self.assertEqual(tax_balance(15894,3,2), -894.44)
	def test_tax_balance_13  (self): self.assertEqual(tax_balance(88000,3,3), 2209.8)
	def test_tax_balance_14  (self): self.assertEqual(tax_balance(88001,3,4), 1729.9)
	def test_tax_balance_15  (self): self.assertEqual(tax_balance(170000.99,3,8), 10176.62)
     
	
	############################################################################
	
# This class digs through AllTests, counts and builds all the tests,
# so that we have an entire test suite that can be run as a group.
class TheTestSuite (unittest.TestSuite):
	# constructor.
	def __init__(self,wants):
		self.num_req = 0
		self.num_ec = 0
		# find all methods that begin with "test".
		fs = []
		for w in wants:
			for func in AllTests.__dict__:
				# append regular tests
				# drop any digits from the end of str(func).
				dropnum = str(func)
				while dropnum[-1] in "1234567890":
					dropnum = dropnum[:-1]
				
				if dropnum==("test_"+w+"_") and (not (dropnum==("test_extra_credit_"+w+"_"))):
					fs.append(AllTests(str(func)))
				if dropnum==("test_extra_credit_"+w+"_") and not BATCH_MODE:
					fs.append(AllTests(str(func)))
		
#		print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
		# call parent class's constructor.
		unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
		# constructor.
		def __init__(self,wants):
			# find all methods that begin with "test_extra_credit_".
			fs = []
			for w in wants:
				for func in AllTests.__dict__:
					if str(func).startswith("test_extra_credit_"+w):
						fs.append(AllTests(str(func)))
		
#			print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
			# call parent class's constructor.
			unittest.TestSuite.__init__(self,fs)

# all (non-directory) file names, regardless of folder depth,
# under the given directory 'dir'.
def files_list(dir):
	this_file = __file__
	if dir==".":
		dir = os.getcwd()
	info = os.walk(dir)
	filenames = []
	for (dirpath,dirnames,filez) in info:
#		print(dirpath,dirnames,filez)
		if dirpath==".":
			continue
		for file in filez:
			if file==this_file:
				continue
			filenames.append(os.path.join(dirpath,file))
#		print(dirpath,dirnames,filez,"\n")
	return filenames

def main():
	if len(sys.argv)<2:
		raise Exception("needed student's file name as command-line argument:"\
			+"\n\t\"python3 testerX.py gmason76_2xx_Px.py\"")
	
	if BATCH_MODE:
		print("BATCH MODE.\n")
		run_all()
		return
		
	else:
		want_all = len(sys.argv) <=2
		wants = []
		# remove batch_mode signifiers from want-candidates.
		want_candidates = sys.argv[2:]
		for i in range(len(want_candidates)-1,-1,-1):
			if want_candidates[i] in ['.'] or os.path.isdir(want_candidates[i]):
				del want_candidates[i]
	
		# set wants and extra_credits to either be the lists of things they want, or all of them when unspecified.
		wants = []
		extra_credits = []
		if not want_all:
			for w in want_candidates:
				if w in REQUIRED_DEFNS:
					wants.append(w)
				elif w in SUB_DEFNS:
					wants.append(w)
				elif w in EXTRA_CREDIT_DEFNS:
					extra_credits.append(w)
				else:
					raise Exception("asked to limit testing to unknown function '%s'."%w)
		else:
			wants = REQUIRED_DEFNS + SUB_DEFNS
			extra_credits = EXTRA_CREDIT_DEFNS
		
		# now that we have parsed the function names to test, run this one file.	
		run_one(wants,extra_credits)	
		return
	return # should be unreachable!	

# only used for non-batch mode, since it does the printing.
# it nicely prints less info when no extra credit was attempted.
def run_one(wants, extra_credits):
	
	has_reqs = len(wants)>0
	has_ec   = len(extra_credits)>0
	
	# make sure they exist.
	passed1 = 0
	passed2 = 0
	tried1 = 0
	tried2 = 0
	
	# only run tests if needed.
	if has_reqs:
		print("\nRunning required definitions:")
		(tag, passed1,tried1) = run_file(sys.argv[1],wants,False)
	if has_ec:
		print("\nRunning extra credit definitions:")
		(tag, passed2,tried2) = run_file(sys.argv[1],extra_credits,True)
	
	# print output based on what we ran.
	if has_reqs and not has_ec:
		print("\n%d/%d Required test cases passed (worth %d each)" % (passed1,tried1,weight_required) )
		print("\nScore based on test cases: %.2f/%d (%.2f*%d) " % (
																passed1*weight_required, 
																total_points_from_tests,
																passed1,
																weight_required
															 ))
	elif has_ec and not has_reqs:
		print("%d/%d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
	else: # has both, we assume.
		print("\n%d / %d Required test cases passed (worth %d each)" % (passed1,tried1,weight_required) )
		print("%d / %d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
		print("\nScore based on test cases: %.2f / %d ( %d * %d + %d * %d) " % (
																passed1*weight_required+passed2*weight_extra_credit, 
																total_points_from_tests,
																passed1,
																weight_required,
																passed2,
																weight_extra_credit
															 ))
	if CURRENTLY_GRADING:
		print("( %d %d %d %d )\n%s" % (passed1,tried1,passed2,tried2,tag))

# only used for batch mode.
def run_all():
		filenames = files_list(sys.argv[1])
		#print(filenames)
		
		wants = REQUIRED_DEFNS + SUB_DEFNS
		extra_credits = EXTRA_CREDIT_DEFNS
		
		results = []
		for filename in filenames:
			print(" Batching on : " +filename)
			# I'd like to use subprocess here, but I can't get it to give me the output when there's an error code returned... TODO for sure.
			lines = os.popen("python3 tester1p.py \""+filename+"\"").readlines()
			
			# delay of shame...
			time.sleep(DELAY_OF_SHAME)
			
			name = os.path.basename(lines[-1])
			stuff =lines[-2].split(" ")[1:-1]
			print("STUFF: ",stuff, "LINES: ", lines)
			(passed_req, tried_req, passed_ec, tried_ec) = stuff
			results.append((lines[-1],int(passed_req), int(tried_req), int(passed_ec), int(tried_ec)))
			continue
		
		print("\n\n\nGRAND RESULTS:\n")
		
			
		for (tag_req, passed_req, tried_req, passed_ec, tried_ec) in results:
			name = os.path.basename(tag_req).strip()
			earned   = passed_req*weight_required + passed_ec*weight_extra_credit
			possible = tried_req *weight_required # + tried_ec *weight_extra_credit
			print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
															name,
															earned,
															possible, 
															(earned/possible)*100,
															passed_req,tried_req,weight_required,
															passed_ec,tried_ec,weight_extra_credit
														  ))
# only used for batch mode.
def run_all_orig():
		filenames = files_list(sys.argv[1])
		#print(filenames)
		
		wants = REQUIRED_DEFNS + SUB_DEFNS
		extra_credits = EXTRA_CREDIT_DEFNS
		
		results = []
		for filename in filenames:
			# wipe out all definitions between users.
			for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS	:
				globals()[fn] = decoy(fn)
				fn = decoy(fn)
			try:
				name = os.path.basename(filename)
				print("\n\n\nRUNNING: "+name)
				(tag_req, passed_req, tried_req) = run_file(filename,wants,False)
				(tag_ec,  passed_ec,  tried_ec ) = run_file(filename,extra_credits,True)
				results.append((tag_req,passed_req,tried_req,tag_ec,passed_ec,tried_ec))
				print(" ###### ", results)
			except SyntaxError as e:
				tag = filename+"_SYNTAX_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except NameError as e:
				tag =filename+"_Name_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except ValueError as e:
				tag = filename+"_VALUE_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except TypeError as e:
				tag = filename+"_TYPE_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except ImportError as e:
				tag = filename+"_IMPORT_ERROR_TRY_AGAIN"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except Exception as e:
				tag = filename+str(e.__reduce__()[0])
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
		
# 			try:
# 				print("\n |||||||||| scrupe: "+str(scruples))
# 			except Exception as e:
# 				print("NO SCRUPE.",e)
# 			scruples = None
		
		print("\n\n\nGRAND RESULTS:\n")
		for (tag_req, passed_req, tried_req, tag_ec, passed_ec, tried_ec) in results:
			name = os.path.basename(tag_req)
			earned   = passed_req*weight_required + passed_ec*weight_extra_credit
			possible = tried_req *weight_required # + tried_ec *weight_extra_credit
			print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
															name,
															earned,
															possible, 
															(earned/possible)*100,
															passed_req,tried_req,weight_required,
															passed_ec,tried_ec,weight_extra_credit
														  ))

def try_copy(filename1, filename2, numTries):
	have_copy = False
	i = 0
	while (not have_copy) and (i < numTries):
		try:
			# move the student's code to a valid file.
			shutil.copy(filename1,filename2)
			
			# wait for file I/O to catch up...
			if(not wait_for_access(filename2, numTries)):
				return False
				
			have_copy = True
		except PermissionError:
			print("Trying to copy "+filename1+", may be locked...")
			i += 1
			time.sleep(1)
		except BaseException as e:
			print("\n\n\n\n\n\ntry-copy saw: "+e)
	
	if(i == numTries):
		return False
	return True

def try_remove(filename, numTries):
	removed = False
	i = 0
	while os.path.exists(filename) and (not removed) and (i < numTries):
		try:
			os.remove(filename)
			removed = True
		except OSError:
			print("Trying to remove "+filename+", may be locked...")
			i += 1
			time.sleep(1)
	if(i == numTries):
		return False
	return True

def wait_for_access(filename, numTries):
	i = 0
	while (not os.path.exists(filename) or not os.access(filename, os.R_OK)) and i < numTries:
		print("Waiting for access to "+filename+", may be locked...")
		time.sleep(1)
		i += 1
	if(i == numTries):
		return False
	return True

# this will group all the tests together, prepare them as 
# a test suite, and run them.
def run_file(filename,wants=None,checking_ec = False):
	if wants==None:
		wants = []
	
	# move the student's code to a valid file.
	if(not try_copy(filename,"student.py", 5)):
		print("Failed to copy " + filename + " to student.py.")
		quit()
		
	# import student's code, and *only* copy over the expected functions
	# for later use.
	import importlib
	count = 0
	while True:
		try:
# 			print("\n\n\nbegin attempt:")
			while True:
				try:
					f = open("student.py","a")
					f.close()
					break
				except:
					pass
# 			print ("\n\nSUCCESS!")
				
			import student
			importlib.reload(student)
			break
		except ImportError as e:
			print("import error getting student... trying again. "+os.getcwd(), os.path.exists("student.py"),e)
			time.sleep(0.5)
			while not os.path.exists("student.py"):
				time.sleep(0.5)
			count+=1
			if count>3:
				raise ImportError("too many attempts at importing!")
		except SyntaxError as e:
			print("SyntaxError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_SYNTAX_ERROR",None, None, None)
		except NameError as e:
			print("NameError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return((filename+"_Name_ERROR",0,1))	
		except ValueError as e:
			print("ValueError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_VALUE_ERROR",0,1)
		except TypeError as e:
			print("TypeError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_TYPE_ERROR",0,1)
		except ImportError as e:			
			print("ImportError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details or try again")
			return((filename+"_IMPORT_ERROR_TRY_AGAIN	",0,1))	
		except Exception as e:
			print("Exception in loading"+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+str(e.__reduce__()[0]),0,1)
	
	# make a global for each expected definition.
	for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS	:
		globals()[fn] = decoy(fn)
		try:
			globals()[fn] = getattr(student,fn)
		except:
			if fn in wants:
				print("\nNO DEFINITION FOR '%s'." % fn)	
	
	if not checking_ec:
		# create an object that can run tests.
		runner = unittest.TextTestRunner()
	
		# define the suite of tests that should be run.
		suite = TheTestSuite(wants)
	
	
		# let the runner run the suite of tests.
		ans = runner.run(suite)
		num_errors   = len(ans.__dict__['errors'])
		num_failures = len(ans.__dict__['failures'])
		num_tests    = ans.__dict__['testsRun']
		num_passed   = num_tests - num_errors - num_failures
		# print(ans)
	
	else:
		# do the same for the extra credit.
		runner = unittest.TextTestRunner()
		suite = TheExtraCreditTestSuite(wants)
		ans = runner.run(suite)
		num_errors   = len(ans.__dict__['errors'])
		num_failures = len(ans.__dict__['failures'])
		num_tests    = ans.__dict__['testsRun']
		num_passed   = num_tests - num_errors - num_failures
		#print(ans)
	
	# remove our temporary file.
	os.remove("student.py")
	if os.path.exists("__pycache__"):
		shutil.rmtree("__pycache__")
	if(not try_remove("student.py", 5)):
		print("Failed to remove " + filename + " to student.py.")
	
	tag = ".".join(filename.split(".")[:-1])
	
	
	return (tag, num_passed, num_tests)


# make a global for each expected definition.
def decoy(name):
		# this can accept any kind/amount of args, and will print a helpful message.
		def failyfail(*args, **kwargs):
			return ("<no '%s' definition was found - missing, or typo perhaps?>" % name)
		return failyfail

# this determines if we were imported (not __main__) or not;
# when we are the one file being run, perform the tests! :)
if __name__ == "__main__":
	main()
