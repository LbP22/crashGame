# launch vue
cd ...\crashGame\frontend

npm ci

npm run serve

# launch backend(in other terminal):
cd ...\crashGame\backend

pipenv sync

pipenv python run crashApp.py
