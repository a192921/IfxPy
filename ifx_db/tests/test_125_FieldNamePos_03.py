# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import ifx_db
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_125_FieldNamePos_03(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_125)

  def run_test_125(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    server = ifx_db.server_info( conn )

    result = ifx_db.exec_immediate(conn, "SELECT * FROM sales")
    result2 = ifx_db.exec_immediate(conn, "SELECT * FROM staff")
    
    for i in range(0, ifx_db.num_fields(result)):
      print "%d:%s" % (i, ifx_db.field_name(result,i))
    
    print "-----"
    
    for i in range(0, ifx_db.num_fields(result2)):
      print "%d:%s" % (i, ifx_db.field_name(result2,i))
    
    print "-----"
    
    if (server.DBMS_NAME[0:3] == 'IDS'):
      print "Region:%s" % ifx_db.field_name(result, 'region')
    else:
      print "Region:%s" % ifx_db.field_name(result, 'REGION')
    print "5:%s" % ifx_db.field_name(result2, 5)

#__END__
#__LUW_EXPECTED__
#0:SALES_DATE
#1:SALES_PERSON
#2:REGION
#3:SALES
#
#-----
#0:ID
#1:NAME
#2:DEPT
#3:JOB
#4:YEARS
#5:SALARY
#6:COMM
#
#-----
#Region:REGION
#5:SALARY
#__ZOS_EXPECTED__
#0:SALES_DATE
#1:SALES_PERSON
#2:REGION
#3:SALES
#
#-----
#0:ID
#1:NAME
#2:DEPT
#3:JOB
#4:YEARS
#5:SALARY
#6:COMM
#
#-----
#Region:REGION
#5:SALARY
#__SYSTEMI_EXPECTED__
#0:SALES_DATE
#1:SALES_PERSON
#2:REGION
#3:SALES
#
#-----
#0:ID
#1:NAME
#2:DEPT
#3:JOB
#4:YEARS
#5:SALARY
#6:COMM
#
#-----
#Region:REGION
#5:SALARY
#__IDS_EXPECTED__
#0:sales_date
#1:sales_person
#2:region
#3:sales
#
#-----
#0:id
#1:name
#2:dept
#3:job
#4:years
#5:salary
#6:comm
#
#-----
#Region:region
#5:salary
