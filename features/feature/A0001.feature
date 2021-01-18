Feature: user login
  Scenario Outline: 获取图形验证码
    Given api api/sc/captcha/captcha
    And param
    """
    scene: "uc_login"
    """
    When GET
    Then JSONPATH_ASSERT "<resultCode>" equals "<result>"
    Then JSONPATH_GET_MONGO
      | key   | value |
      | $.data | resultData |
    Examples:
      | resultCode | result |
      | result    | 000000 |
  Scenario Outline: 用户登录
    Given api api/uc/login
    And param
    """
    userLoginpwd: "123456qqQQ"
    captcha: ${resultData}
    userMobile: ""
    userLoginname: "YL015359"
    verify: ""
    userEmail: ""
    """
    When GET
    Then JSONPATH_ASSERT "<resultCode>" equals "<result>"
    Then JSONPATH_GET_MONGO
      | key   | value |
      | $.data.token | token |
    Examples:
      | resultCode | result |
      | result     | 000000 |
