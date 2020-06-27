import check
def main(scode,name):
    obcode="public class Main{    public static void main(String args[])    {        "+name+" ob = new "+name+"();        String arr[]={};        ob.main(arr);    }}"
    fnl=obcode+scode
    fnl=check.base_64_encoder(obcode+scode)
    return fnl