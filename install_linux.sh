echo 'Installing virtual environment...'
python3 -m venv venv
echo '...successfully installed.'
echo ''
echo 'Activating virtual environment...'
. ./venv/bin/activate
echo '...successfully activated.'
echo ''
echo 'Installing requirements...'
pip3 install -r requirements.txt
echo ''
. ./venv/bin/activate
echo 'Installation complete. Enjoy!'