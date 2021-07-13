# HtmlUnit Selenium Server

That's the [docker image](https://hub.docker.com/repository/docker/goshkalp/htmlunit_selenium_server) 
of htmlunit server based on [Selenium Server](http://selenium.dev/) version `3.141.59` and
[HtmlUnit Driver](https://github.com/SeleniumHQ/htmlunit-driver) version `2.51.0`.

## Quick start
Using Docker CLI:
```
docker run \
    -d \ 
    -p 127.0.0.1:4444:4444 \
    htmlunit_selenium_server
```

## Next steps
After starting the server you can test you sites with selenium api
using any programming language.  
Python example:
```
from selenium.webdriver import Remote
from selenium.webdriver import DesiredCapabilities

capabilities = DesiredCapabilities.HTMLUNITWITHJS.copy()

driver = Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=capabilities)
```

## Simplification of work
You can use the ready-made [Python script](https://github.com/GoshkaLP/htmlunit_selenium_server/blob/master/WebDriverHandler.py) to make your tests. The script has presets for easier work when testing sites.  
Example of script usage:
```
proxy = {'https': 'https://user:pass@ip:port'}
driver = WebDriverHandler(js_support=True, proxy_options=proxy)
driver.start_driver()
print(driver.get('https://api.my-ip.io/ip'))
```

## Related links
- http://selenium.dev/
- https://github.com/HtmlUnit/htmlunit
- https://github.com/SeleniumHQ/htmlunit-driver
- https://github.com/GoshkaLP/htmlunit_selenium_server
- https://hub.docker.com/repository/docker/goshkalp/htmlunit_selenium_server

## License
This image and script are distributed under Apache License 2.0.