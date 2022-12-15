import openai
import os
import streamlit as sl

org = sl.text_input("Enter OpenAI Organisation string")
the_key = sl.text_input("Enter OpenAI API key")

openai.organization = org
openai.api_key = the_key

temp = sl.sidebar.slider("Craziness of ideas",0.0,1.0,0.5)
scenario = sl.text_input("Enter scenario  event e.g 'power failure in ...'")

go = sl.button("do it!")

if go:
    sl.sidebar.text("Drafting scenario")

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="write a three-act crisis scenario about a"+scenario,
      temperature=temp,
      max_tokens=1000,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )

    AI_scenario = response["choices"][0]["text"]




    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="shorten to a single sentance '" + AI_scenario+"'",
        temperature=temp,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    AI_precise = response["choices"][0]["text"]


    sl.sidebar.text("Drafting stakeholders")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="write a list of stakeholders in the scenario '" + AI_scenario+"'",
        temperature=temp,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    AI_stakeholders = response["choices"][0]["text"]

    sl.sidebar.text("Drafting case data")
    #case data
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="write a list of possible case data required for the scenario '" + AI_scenario+"'",
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    AI_case_data = response["choices"][0]["text"]

    #key decisions
    sl.sidebar.text("Drafting key decisions")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="write a list of key decisions for the training audience exercising with the scenario '" + AI_scenario+"'",
        temperature=temp,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    AI_key_decisions = response["choices"][0]["text"]

    sl.sidebar.text("Drafting training objectives")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="write a list of training objectives for a crisis exercise about '" + AI_scenario+"'",
        temperature=temp,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    AI_trainingobjectives = response["choices"][0]["text"]


    sl.sidebar.text("Drafting rich media ideas")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="write a list of rich media communications channels for '" + AI_scenario+"'",
        temperature=temp,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    AI_richmedia = response["choices"][0]["text"]


    sl.sidebar.text("Drafting breaking news")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="write a breaking newscast for '" + AI_precise+"'",
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    AI_breakingnews = response["choices"][0]["text"]

    sl.sidebar.text("Drafting tweets")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="write ten Tweets from customers complaining about '" + AI_scenario+"'",
        temperature=temp,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    AI_tweets = response["choices"][0]["text"]


    sl.subheader("Summary")
    sl.write(AI_precise)

    sl.subheader("Three Acts")
    sl.write(AI_scenario)

    sl.subheader("Stakeholders")
    sl.write(AI_stakeholders)

    sl.subheader("Possible case Data required")
    sl.write(AI_case_data)

    sl.subheader("Possible training audience key decisions")
    sl.write(AI_key_decisions)

    sl.subheader("Possible training objectives")
    sl.write(AI_trainingobjectives)

    sl.subheader("Possible rich media")
    sl.write(AI_richmedia)

    sl.header("Content")
    sl.subheader("Breaking news")
    sl.write(AI_breakingnews)

    sl.subheader("Tweets")
    sl.write(AI_tweets)