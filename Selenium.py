from selenium import webdriver

# Запуск браузера (убедитесь, что ChromeDriver установлен и доступен в PATH)
driver = webdriver.Chrome()

# Открытие главной страницы Google
driver.get("https://www.google.com")

# Ожидаем несколько секунд, чтобы страница успела загрузиться
input("Нажмите Enter, чтобы закрыть браузер...")

# Закрываем браузер
driver.quit()
