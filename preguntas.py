"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    return tbl0.shape[0]


def pregunta_02():
    return tbl0.shape[1]


def pregunta_03():
    return tbl0['_c1'].value_counts().sort_index()


def pregunta_04():
    return tbl0.groupby('_c1')['_c2'].mean()


def pregunta_05():
    return tbl0.groupby('_c1')['_c2'].max()


def pregunta_06():
    return tbl1['_c4'].str.upper().unique()


def pregunta_07():
    return tbl0.groupby('_c1')['_c2'].sum()


def pregunta_08():
    return tbl0['_c0']+tbl0['_c2']


def pregunta_09():
    return tbl0['_c3'].map(lambda x: x.split('-')[0])


def pregunta_10():
    def fun(x):
        lista_c2=sorted(list(x))
        cadena_c2=""
        for i in lista_c2:        
            cadena_c2+=str(i)+":"
        return cadena_c2[:-1]
    cadena_c1_c2=tbl0.groupby('_c1')['_c2'].apply(lambda x: fun(x)) 
    return pd.DataFrame(cadena_c1_c2, columns=['_c2'])


def pregunta_11():
    def fun_11(x):
        lista_c4=sorted(list(x))
        cadena_c4=""
        for i in lista_c4:
            cadena_c4+=str(i)+","
        return cadena_c4[:-1]
    cadena_c0_c4=tbl1.groupby('_c0')['_c4'].apply(lambda x: fun_11(x))
    cadena_c0_c4=pd.DataFrame(cadena_c0_c4, columns=['_c4'])
    cadena_c0_c4.reset_index(inplace=True)
    return cadena_c0_c4


def pregunta_12():
    def fun_12(x):
        _c5a=list(x['_c5a'])
        _c5b=list(x['_c5b'])
        cadena=[_c5a[i]+':'+str(_c5b[i]) for i in range(len(_c5a))]
        cadena=sorted(cadena)
        cadena_c5a_c5b=""
        for i in cadena:
            cadena_c5a_c5b+=i+','
        return cadena_c5a_c5b[:-1]
    cadena_c0_c5a_c5b=tbl2.groupby('_c0')[['_c5a','_c5b']].apply(lambda x: fun_12(x))
    cadena_c0_c5a_c5b=pd.DataFrame(cadena_c0_c5a_c5b, columns=['_c5'])
    cadena_c0_c5a_c5b.reset_index(inplace=True)
    return cadena_c0_c5a_c5b


def pregunta_13():
    df_tbl0_c1_tbl2_c5b=pd.merge(tbl0[['_c0','_c1']],tbl2[['_c0','_c5b']])
    tbl0_c1_tbl2_c5b_sum=df_tbl0_c1_tbl2_c5b.groupby('_c1')['_c5b'].sum()
    return tbl0_c1_tbl2_c5b_sum
