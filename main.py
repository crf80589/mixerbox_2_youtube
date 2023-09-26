# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import json

# read mixerbox backup playlist
with open('./mixerbox_library.txt','r',encoding="utf-8") as file:
    result = json.loads(file.read())

for i in result:
    # read my list
    if i['key'] == 'my_playlist':
        for playlist in i['content']:
            # this is playlist title
            playlist_name = (playlist['name'])
            ["xUUjIyWJh3A","LbiWaeLdqeA","RzXTe-QfWTw","X3Ma2vhc-M0","OhHvXIArJMY","4G-iYTkmV20","OWJGFuJ7Pzc","Q4CFUoMEsxY","nFR3uXaR0wk","feOq6MWeUXA","bNC0HXdaDig","JqbHznsGe6I","zuoVd2QNxJo","7HDeem-JaSY","1CSLawtNFRg","Jy5g8i90SjU","ey7Jph8ndJU","woKq2sD8xho","AfFpsCz-aoY","Etq_BEjQE10","gPqfGpLxVIU","xIa4GRcUooo","5mNrRVp-SBc","eZh1mC1vPgw","rvPIE9ZWePw","LAM_25pQ8ls","gcgKUcJKxIs","LUMyDexBxFo","hHC208KAZLo","uCFLjXE2LtA","DdF-u3fe5pg","07hpRRx4xMg","razQj9VbzwE","PrIANT3FJLE","iurGYDQnqFo","aZjV2UkgFRk","qo55wGLXcOQ","qD1kP_nJU3o","To7qHHaTl0s","Sbi-tvO5KgQ","aOKa-5AHCtU","ljd9ISixsWo","wukVNyIrtMc","9XkvsAJ0Ceg","qmr496mJb6w","55zeL4ptZT0","m1XHGGpIQOk","L6PflJIYdG8","AX9bl_S5oZw","BEpzzljK2bo","NdiB-59DG34","okVTSehE414","s4Ow55AbdCg","TBkybgllGRA","6vn1-BCb1XY","1hI-7vj2FhE","gCQuEakOEFo","RccDIpx4ZMM","NHXUM-6a3dU","lc-ce20XRdg","jEojOmwDap4","KbGPM9jFeGg","V91B6aQOn4k","ulKrn-3GraI","ytQhhgHGj_s","5mNrRVp-SBc","ArmDp-zijuc","w3rOAlK26ts","J9ys5dJ1dE8","0bIRwBpBcZQ","AjaHWJl6EC8","Fx3449cEohg","JAbCuo0UUM8","sXGGJpUX9R8","5BPH6FoiYuQ","-uqWaGzQyxA","AbZH7XWDW_k","APgx1k-2Tqc","o5LX1mEPJtg","4jWzGkRsHw8","7CgVQPwd9M8","In0cTkWF9WA","wDsO97LiutM","596LjZWH5hg","BSlMAJ7SkMA","VV5PT9eO3rM","8uZGBbic0a4","wG7VOLDjL6k","Auf_JaLHQMw","_QpJlDoI-Cc","JflOKxCx97o","I4lonGT1PYM","hN5MBlGv2Ac","pG6iaOMV46I","yXZd7xVdpJ0","hwENuZHFTj0","3-ptVHZZdBg","BVK_Q6KZSUI","jOTfBlKSQYY","8rueHdrzRRs","F4vGFscB_fg","edTQsoNcADA","Dl-ygwweQEc","1YWmCiWCxlE","TbFWYT9VGRk","rxpubZXi0sE","X2njc8is50o","-ceYSag6AIE","L229QDxDakU","kXYiU_JCYtU","86wypSCXK9M","F_dGEjzRG_Y","VS_1h8iIsRY","1emA1EFsPMM","te9Pfsugz6U","cB7DIIG0ykk","RPWDeLqsN0g","0z2i9ywFtgI","m78lJuzftcc","mQUek1GYfvs","9tN1xixvYOc","COS0pHrCi0k","-T-2tf9OYcc","KOLDiXnQC7Q","hmyEkTioX5E","70RTxbhqj5s","2BrzK4fZ45k","xVvsm8qRhQs","NanLw5v2v7U","8R3ZHHbVvR8","bCB_nIdN86s","OBYprTfpwAw","mebzXfWi87E","QC1yP4QrsyA","VaAacrLk4gE","oec9R5ypf-o","z_iMEjTJsBE","IHw3UuECE1c","uW0ag9ajpsI","WY6nQK7zbsk","x4s-th4N2og","ynaARgs_yvQ","XtbQHPRCLq0","-Rp7UPbhErE","5TCz-Z7hV-4","0TJrheSXuPc","be2wvNFTLMc","HwF1i_6Iwp8","efmtFFnZOGA","yLb1gJy6Ku4","WOWybmnASlg","19m_Y531sX8","wgwIfD9Ihik","04VXfavbeDs","6VCpmBYAKXI","fYqeSZoNqqA","x3bDhtuC5yk","kfXdP7nZIiE","zsYSSVoQnP4","R2V9sHAlLuQ","4OrCA1OInoo","bu7nU9Mhpyo","F5RE_S8aIF8","FGDL_gx9bgc","BsvIwqyiaJw","qswX-4yDiV4","kLvnet_N3ZM","VvycFWLSdIs","_QAQNM39Qxk","_VxLOj3TB5k","PXmGrkEtxrc","1CcQDuuhdXA","7mVTAWQKgFk","2pXXjBe1fXo","4iRupuNet3Q","aZp-4C0mtws","Au3OyYS4bI8","hlJ1hpfREbQ","a8-9we0HjA4","Fn7NLWHJw4s","phz0TIk_z94","ugVNDvnDDpA","gFxuJqdJW5E","5FK0qCEQ3L0","ovzPtweLM8A","sGJv2a3_rY8","CO3ij6BvjHA","2BEFukvLZfI","EzURHl-VCRo","AUp8MZbkQfI","GCgvpwLNvtY","kiSYRbMn67I","6Y-QIhEEaGc","QaLFW4bHQSY","mGeiABBB5f8","jj-8twO9KUA","-Q7wCx7T7Yc","lzKBvl_7QqQ","UrJvkWzOyV0","HK7SPnGSxLM","5NiSANTO-PM","RZG02MIb1VE","KKbdUiBeYGU","TMk6pYwhPMk","cVBkGaQqmIQ","6aPAXGhmML0","Df9lbCJNhGU","DBcVPsTmG5I","ma7r2HGqwXs","ugA9AUagOH4","gEc8Ugb5LF4","Ej0naFw91NU","Hlp8XD0R5qo","tOep1yAuYEY","A3xx6M-ZNbk","Ed-8UTHVz-k","mbqhovfTTg8","e3Qu5C0pcGA","-7uaa_ONFo0","rBBQzO411bA","5J4mRbVCYrk","Qd33i-OoOk4","rgTQYCo0WCM","1BBw4oyOMG0","KiJUDlwwznE","qJMsVNleCw4","NRt-Y7CHWY8","fl1Wbd-ldMQ","evavdUeZUno","ezTI-7oBCAM","MqnF7th-grc","rhcc1KQlCS4","FWtbGkpdoP4","bG563p_moiE","NwwuIJBH7Bg","B5E5HkV8ukI","sUzAmh5butc","FQ7Sj3C_T8E","UuTBI3MY_ic","jJpAGm3e2Tg","bpJko9n8KTY","i8cptH7f7lE","7XlqcS6B7WA","8K8Y_n-CY08","5dyyrbtxC4E","-7H5ug_XP4E","6O_Zx9St9ik","3mEeKAdXAo4","GE7A3jXDH3I","uOkuyk_VzmU","8MG--WuNW1Y","TsKRnpBGZro","PU8tlXAy5os","6s2s-xWxVHc","Ryjh-YcO4ag","A759eDYocB0","EGZeNp87PXg","6Xu-TGL-_qk","E9Th_UeOfgI","SMwul9FkT7w","Ej83dvkU-Z4","y1kzYlBx6xE","hhpi-ZryYSo","H059kI52_rE","E1ybIxGYhwQ","H-4HFyGs3NY","PJJhHihvDpo","K3R2JTNk3us","B5ner2-oBGQ","paecvB1-uPE","caxiOmSWWEM","1a7V8zwbD8o","37uw4W2MwgU","0rp3pP2Xwhs","rTCwL0Wsvyw","jL6D7rqk4SQ","f6tU6BfnWEI","7Jhdn2riuC0","VVWQ12-Cf_4","gdWS0Xuc088"]}]}]
            with open('./'+playlist_name+'.txt','a',encoding='utf-8') as f : 
                for playlist_music in playlist['content']:
                    # playlist content is url code
                    url = 'https://www.youtube.com/watch?v='+playlist_music
                    # pyquery
                    doc = pq(url=url,encoding='utf-8')
                    # get youtube title
                    title = doc('meta[name=title]').attr('content')
                    print(title)
                    if title != '':
                        # write youtube title to playlist txt
                        f.write(title+'\r')
