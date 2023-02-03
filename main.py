'''
Copyright [2023] [QingYu]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import core.login_SignUp as ls
from json import load,dumps

lss=ls.login_signup()
with open('./settings.json','r') as f:
    opent=load(f)
if opent["open"] == 0:
    lss.signup()
    with open('./settings.json', 'r') as f:
        opent = load(f)
        f.seek(0)
        f.truncate()
        opent["open"] = 1
        data = dumps(opent)
        f.write(data)

else:
    lss.LoginUI()

