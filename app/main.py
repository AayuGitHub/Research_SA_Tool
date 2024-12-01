'''
Hare Krishna, Hare Krishna Krishna Krishna Hare Hare, Hare Rama Hare Rama Rama Rama Hare Hare
Best Wishes from Shelly And Aayush
'''

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
  return {"Message": "welcome to the tool Analysis API"}
