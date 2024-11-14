from behave import *
from soma import soma

@given(u'Primeiro valor será 5')
def step_impl(context):
    context.num1 = 5

@given(u'Segundo valor será 2')
def step_impl(context):
    context.num2 = 2

@when(u'Executa a função')
def step_impl(context):
    context.saida = soma(context.num1, context.num2)

@then(u'Saída deverá ser o valor 7')
def step_impl(context):
    context.saida == 7