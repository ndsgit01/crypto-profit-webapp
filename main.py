#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:47:06 2022

@author: ndsbits
"""
from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
import io
import base64

import crypto


import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt     

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", 
                                      {"request": request})

@app.post("/show_plot")
async def show_plot(request: Request, tickers: str = Form(...)):
    tickers = [ticker.strip() for ticker in tickers.split(',')]
    ticker_profits = {ticker: crypto.get_profits(ticker) 
                      for ticker in tickers}
    fig = plt.figure()
    for ticker in tickers:
        plt.plot(ticker_profits[ticker])
    plt.ylabel('profit %')
    plt.xlabel('day number')
    plt.legend(tickers)
    pngImage = io.BytesIO()
    fig.savefig(pngImage)
    pngImageB64String = \
        base64.b64encode(pngImage.getvalue()).decode('ascii')
    scores = {ticker: ticker_profits[ticker][-1] for ticker in tickers}
    return templates.TemplateResponse("plot.html", 
                                      {"request": request,
                                       "scores":scores,
                                       "picture": pngImageB64String})
    
    



