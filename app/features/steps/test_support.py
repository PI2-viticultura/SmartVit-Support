from behave import given, when, then
import requests

request_headers = {}
request_bodies = {}
api_url = None


@given('a pagina de registro do suporte')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-support-stg.herokuapp.com/support'
    print('url :'+api_url)


@when('ele registar os campos do suporte')
def step_impl_when(context):
    request_bodies['POST'] = {"priority": "baixa",
                              "problem": "Sistema eletrônico com defeito",
                              "description": "sistema esta aquecendo muito"}
    response = requests.post(
                             api_url,
                             json=request_bodies['POST']
                            )
    assert response.status_code == 200


@then('os dados devem passar pelo servico atraves do BFF e armazenar no banco')
def step_impl_then(context):
    api_bff_url = 'https://smartvit-user-bff-dev.herokuapp.com/support/'
    response = requests.post(
                            api_bff_url,
                            json=request_bodies['POST']
                            )
    assert response.status_code == 200
