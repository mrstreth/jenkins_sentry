from typing import Union

# необходимая настройка и импорт модулей
import sentry_sdk
sentry_sdk.init("https://8a1d87e02e734caab36501a3c56ba41c@o387100.ingest.sentry.io/5221989")

# установка тегов
from sentry_sdk import configure_scope
with configure_scope() as scope:
    scope.user = {'email':'mr.tesanta@gmail.com'}
    scope.set_tag("JENKINS","lab6")
    scope.set_tag("author","mrstreth")

answer : Union[int, float] # анотация типа (не обязательна)	

try:
    answer = 1 / 0
except:
    answer = 1 / 1
finally:
    #print(f'answer = {answer}')
    print('answer =', answer)
