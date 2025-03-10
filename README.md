Step 1: Clone the Repository

To clone your repository, use the following command in Google Colab:

!git clone https://github.com/mahfujurc/grd.git

Step 2: Navigate to the Cloned Directory

Once the repository is cloned, navigate to the grd directory:

%cd grd

Step 3: Install the Required Dependencies

After navigating to the grd directory, install any dependencies specified in the requirements.txt (if it exists):

!pip install -r requirements.txt

If there is no requirements.txt file, you can install Gradio directly:

!pip install gradio

Step 4: Run Your calculator.py Script

Now, run your calculator.py script to start the Gradio interface:

!python3 calculator.py

Gradio will provide a link in the output. You can click that link to interact with the calculator interface in your browser.









Step 1: Upgrade Gradio to the Latest Version

Since you're using Gradio version 3.1.0 and Gradio 4.44.1 is available, you can upgrade Gradio to the latest version by running this command in collab:

!pip install --upgrade gradio
