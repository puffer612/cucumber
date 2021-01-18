Feature:
  Scenario Outline: call interface withOut userId
  Given api http://192.168.10.102:7010/icall/call
  And param
  """
  eeUserId: ""
  eeCallouttype: "C"
  phoneNumber: "bkhpCAiQaPC+wwRjwfmZug=="
  scene: ""
  """
  And Cookiex is a table
  | key   | value |
  | TOKEN | ${token} |
  When GET
  Then JSONPATH_ASSERT "<resultCode>" equals "<code>"
  Examples:
  | resultCode | code    |
  | result     | GB2001 |