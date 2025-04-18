# Automate a Google search for 'news', take a screenshot, and close the browser
r.init(visual_automation=True, chrome_browser=True)
r.url('https://www.google.com/')
r.type('//*[@name="q"]', 'news')
r.click('//*[@name="btnK"]')
r.wait(5)
r.snap('page', 'Captured_Image.png')
r.close()
# This will save a screenshot named 'Captured_Image.png' of the search results.