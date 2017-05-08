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

  def test_159a_FetchAssocSeveralRows_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_159a)

  def run_test_159a(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)

    server = ifx_db.server_info( conn )
    if (server.DBMS_NAME[0:3] == 'IDS'):
      op = {ifx_db.ATTR_CASE: ifx_db.CASE_UPPER}
      ifx_db.set_option(conn, op, 1)

    result = ifx_db.exec_immediate(conn, "select prstdate,prendate from project")
    i = 1
    
    row = ifx_db.fetch_assoc(result)
    while ( row ):
      #printf("%3d %10s %10s\n",i, row['PRSTDATE'], row['PRENDATE'])
      print "%3d %10s %10s" % (i, row['PRSTDATE'], row['PRENDATE'])
      i += 1
      row = ifx_db.fetch_assoc(result)

#__END__
#__LUW_EXPECTED__
#  1 1982-01-01 1983-02-01
#  2 1982-01-01 1983-02-01
#  3 1982-01-01 1983-02-01
#  4 1982-01-01 1983-02-01
#  5 1982-01-01 1983-02-01
#  6 1982-01-01 1983-02-01
#  7 1982-01-01 1983-02-01
#  8 1982-01-01 1983-02-01
#  9 1982-01-01 1983-02-01
# 10 1982-01-01 1982-12-01
# 11 1982-01-01 1982-12-01
# 12 1982-02-15 1982-12-01
# 13 1982-01-01 1983-02-01
# 14 1982-01-01 1983-02-01
# 15 1982-01-01 1983-02-01
# 16 1982-01-01 1983-02-01
# 17 1982-01-01 1983-02-01
# 18 1982-01-01 1983-02-01
# 19 1982-01-01 1983-02-01
# 20 1982-01-01 1982-09-15
#__ZOS_EXPECTED__
#  1 1982-01-01 1983-02-01
#  2 1982-01-01 1983-02-01
#  3 1982-01-01 1983-02-01
#  4 1982-01-01 1983-02-01
#  5 1982-01-01 1983-02-01
#  6 1982-01-01 1983-02-01
#  7 1982-01-01 1983-02-01
#  8 1982-01-01 1983-02-01
#  9 1982-01-01 1983-02-01
# 10 1982-01-01 1982-12-01
# 11 1982-01-01 1982-12-01
# 12 1982-02-15 1982-12-01
# 13 1982-01-01 1983-02-01
# 14 1982-01-01 1983-02-01
# 15 1982-01-01 1983-02-01
# 16 1982-01-01 1983-02-01
# 17 1982-01-01 1983-02-01
# 18 1982-01-01 1983-02-01
# 19 1982-01-01 1983-02-01
# 20 1982-01-01 1982-09-15
#__SYSTEMI_EXPECTED__
#  1 1982-01-01 1983-02-01
#  2 1982-01-01 1983-02-01
#  3 1982-01-01 1983-02-01
#  4 1982-01-01 1983-02-01
#  5 1982-01-01 1983-02-01
#  6 1982-01-01 1983-02-01
#  7 1982-01-01 1983-02-01
#  8 1982-01-01 1983-02-01
#  9 1982-01-01 1983-02-01
# 10 1982-01-01 1982-12-01
# 11 1982-01-01 1982-12-01
# 12 1982-02-15 1982-12-01
# 13 1982-01-01 1983-02-01
# 14 1982-01-01 1983-02-01
# 15 1982-01-01 1983-02-01
# 16 1982-01-01 1983-02-01
# 17 1982-01-01 1983-02-01
# 18 1982-01-01 1983-02-01
# 19 1982-01-01 1983-02-01
# 20 1982-01-01 1982-09-15
#__IDS_EXPECTED__
#  1 1982-01-01 1983-02-01
#  2 1982-01-01 1983-02-01
#  3 1982-01-01 1983-02-01
#  4 1982-01-01 1983-02-01
#  5 1982-01-01 1983-02-01
#  6 1982-01-01 1983-02-01
#  7 1982-01-01 1983-02-01
#  8 1982-01-01 1983-02-01
#  9 1982-01-01 1983-02-01
# 10 1982-01-01 1982-12-01
# 11 1982-01-01 1982-12-01
# 12 1982-02-15 1982-12-01
# 13 1982-01-01 1983-02-01
# 14 1982-01-01 1983-02-01
# 15 1982-01-01 1983-02-01
# 16 1982-01-01 1983-02-01
# 17 1982-01-01 1983-02-01
# 18 1982-01-01 1983-02-01
# 19 1982-01-01 1983-02-01
# 20 1982-01-01 1982-09-15
