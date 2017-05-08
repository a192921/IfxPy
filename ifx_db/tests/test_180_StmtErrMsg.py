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

  def test_180_StmtErrMsg(self):
    obj = IfxDbTestFunctions()
    obj.assert_expectf(self.run_test_180)

  def run_test_180(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    if conn:
      result = ''
      result2 = ''
      try:
        result = ifx_db.exec_immediate(conn,"insert int0 t_string values(123,1.222333,'one to one')")
      except:
        pass
      if result:
        cols = ifx_db.num_fields(result)
        print "col:", cols,", " 
        rows = ifx_db.num_rows(result)
        print "affected row:", rows
      else:
        print ifx_db.stmt_errormsg()
      try:
        result = ifx_db.exec_immediate(conn,"delete from t_string where a=123")
      except:
        pass
      if result:
        cols = ifx_db.num_fields(result)
        print "col:", cols,", "
        rows = ifx_db.num_rows(result)
        print "affected row:", rows
      else:
        print ifx_db.stmt_errormsg()
    
    else:
      print "no connection"

#__END__
#__LUW_EXPECTED__
#[IBM][CLI Driver][DB2/%s] SQL0104N  An unexpected token "insert int0 t_string" was found following "BEGIN-OF-STATEMENT".  Expected tokens may include:  "<space>".  SQLSTATE=42601 SQLCODE=-104col: 0 , affected row: 0
#__ZOS_EXPECTED__
#[IBM][CLI Driver][DB2%s] SQL0104N  An unexpected token "INT0" was found following "".  Expected tokens may include:  "INTO".  SQLSTATE=42601 SQLCODE=-104col: 0 , affected row: 0
#__SYSTEMI_EXPECTED__
#[IBM][CLI Driver][AS] SQL0104N  An unexpected token "INT0" was found following "".  Expected tokens may include:  "INTO".  SQLSTATE=42601 SQLCODE=-104col: 0 , affected row: 0
#__IDS_EXPECTED__
#[IBM][CLI Driver][IDS/%s] A syntax error has occurred. SQLCODE=-201col: 0 , affected row: 0
