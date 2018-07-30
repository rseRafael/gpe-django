from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_protect

def uploadfile(req):
    print(req.method)
    if req.method == 'POST':
        print(req.POST)
        print(req.FILES)
        if req.FILES:
            f = req.FILES['file1']
            print(f)
            print(dir(f))
            for prop in dir(f):
                try:
                    eval("print(type(f.{0}), '{1}')".format(prop, prop))
                except Exception as err:
                    pass

                
            '''
            try:
                F = f.open('rb')
                a = F.readlines()
                F.close()
                F = open(file= "/home/rafael/Desktop/testfile", mode='ab')
                for prop in a:
                    F.write(prop)
                F.close()
            except Exception as err:
                print(err)
            finally:
                return HttpResponseRedirect('/app1/render/sucesso/')
            '''
            return HttpResponseRedirect('/app1/render/sucesso/')
        else:
            return HttpResponseRedirect('/app1/render/falhou/')
    else:
        form = UploadFileForm()
    return render(req, 'forms.html', {'forms': form})

def test(req, msg):
    try:
        pass
    except Exception as err:
        print(err)
    return HttpResponse(msg)

@csrf_protect
def formulario(req):
    c = {}
    return render_to_response('app1/forms.html', c)
