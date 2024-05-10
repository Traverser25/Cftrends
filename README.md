# CFtrends

CFtrends is a web application designed to keep users updated with fresh Codeforces (CF) problems from the last year. It continuously fetches new problems, allowing users to stay in touch with emerging trends in competitive programming.

## Features

- **Continuous Updates:** CFtrends fetches new CF problems regularly, ensuring that users have access to the latest challenges.
- **Single-Page HTML Website:** The website is designed to be lightweight and easy to navigate, providing a seamless user experience.
- **Flask-based Backend:** CFtrends is built on Flask, a lightweight web application framework for Python, making it easy to develop and maintain.
- **SQLite3 Database:** Problem details are stored in an SQLite3 database, enabling efficient data retrieval and management.
- **Web Scraping:** CFtrends employs web scraping techniques to gather new problems
- 
Make sure you have the following dependencies installed:
- Flask
- Flask-CORS
- BeautifulSoup4

3. **Run the Application:**
Start the Flask application by running the `app.py` file:

4. **Access the Website:**
Open your web browser and go to `http://localhost:5000` to access CFtrends.

## Database

CFtrends uses SQLite3 as its database. The database file (`CFproblems.db`) is provided in the repository. It contains tables for storing problem details.

## Scraping New Problems

To update the database with new problems, you can use the `scrapProb.py` script provided in the repository. Make sure to install any additional dependencies required for web scraping if needed.

## Contributing

Contributions to CFtrends are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy Coding with CFtrends!
