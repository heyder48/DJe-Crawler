import urllib3
import os
import shutil

def downloadFile(fileUrl,NomeArquivo,diretory):
    http = urllib3.PoolManager()

    file_path = os.path.join(diretory,NomeArquivo)

    if not os.path.isdir(diretory):
        os.makedirs(diretory)
    try:
        with http.request('GET',fileUrl, preload_content = False) as resp, open(file_path, 'wb') as out:
            shutil.copyfileobj(resp,out)
        resp.release_conn()
    except:
        raise