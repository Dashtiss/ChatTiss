# Chattiss - README

Chattiss is a chatbot project that allows users to enter their questions or statements in a text box, and then sends a request to ChatGPT, a large language model trained by OpenAI. ChatGPT generates a response based on the user's input, which is then displayed on the screen.

## Installation

### Using Hosted Site

To use Chattiss, you can navigate to the hosted site in your web browser and start using the text box. No installation is necessary.

### Hosting Your Own Chattiss

If you want to host your own version of Chattiss, you can follow these steps:

1. Download the Chattiss source code from the Github repository.
2. Install the required packages by running `pip install -r requirements.txt` or `pip3 install -r requirements.txt` in your terminal or command prompt.
3. Start the Flask web server by running `python app.py` in your terminal or command prompt.
4. Open your web browser and go to `http://localhost:5000` to access Chattiss.

Note: If you want to deploy Chattiss on a remote server, you will need to modify the `app.py` file to listen on the appropriate IP address and port number. You may also need to configure your server to allow incoming traffic on the port number you choose.

## Credits

Chattiss was developed by Dashtiss. The project uses ChatGPT, which was developed by OpenAI. The site was created as a demonstration of how ChatGPT can be used to generate responses to user input.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
