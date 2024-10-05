import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class OWASPBrowsingTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        # To store bookmarks and history
        self.bookmarks = []
        self.history = []

        # Set main window properties
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Create the toolbar
        self.create_toolbar()

        # Update history when URL changes
        self.browser.urlChanged.connect(self.update_history)

    def create_toolbar(self):
        # Creating a toolbar with various actions
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        toolbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        toolbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        toolbar.addAction(reload_btn)

        # Home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        toolbar.addAction(home_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.url_bar)

        # Developer tools button
        devtools_btn = QAction('Developer Tools', self)
        devtools_btn.triggered.connect(self.open_developer_tools)
        toolbar.addAction(devtools_btn)

        # Bookmarks button
        bookmarks_btn = QAction('Bookmarks', self)
        bookmarks_btn.triggered.connect(self.show_bookmarks)
        toolbar.addAction(bookmarks_btn)

        # Downloads button
        downloads_btn = QAction('Downloads', self)
        downloads_btn.triggered.connect(self.show_downloads)
        toolbar.addAction(downloads_btn)

        # History button
        history_btn = QAction('History', self)
        history_btn.triggered.connect(self.show_history)
        toolbar.addAction(history_btn)

        # SQL Injection Tool button
        sql_injection_btn = QAction('SQL Injection Tool', self)
        sql_injection_btn.triggered.connect(self.open_sql_injection_tool)
        toolbar.addAction(sql_injection_btn)

    # Navigate to home page
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    # Navigate to the typed URL
    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    # Update the URL in the address bar
    def update_url(self, q):
        self.url_bar.setText(q.toString())

    # Update history when the URL changes
    def update_history(self, q):
        url = q.toString()
        if url not in self.history:
            self.history.append(url)

    # Open Developer Tools
    def open_developer_tools(self):
        self.browser.page().runJavaScript('console.log("Opening Developer Tools")')  # Placeholder
        self.browser.page().view().show()  # Show the dev tools (just an example, may not work)

    # Show bookmarks
    def show_bookmarks(self):
        QMessageBox.information(self, "Bookmarks",
                                "\n".join(self.bookmarks) if self.bookmarks else "No bookmarks saved.")

    # Show download manager (placeholder functionality)
    def show_downloads(self):
        QMessageBox.information(self, "Downloads", "No downloads functionality yet.")

    # Show history
    def show_history(self):
        QMessageBox.information(self, "History", "\n".join(self.history) if self.history else "No history recorded.")

    # Placeholder for SQL Injection Tool
    def open_sql_injection_tool(self):
        QMessageBox.information(self, "SQL Injection Tool", "Open SQL Injection Testing Tool")


# Main application loop
app = QApplication(sys.argv)
window = OWASPBrowsingTool()
window.setWindowTitle("OWASP Mantra-Like Browser")
app.exec_()
