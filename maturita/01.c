

int main(void){
    int a,b,c;
    a=b=c=0;
    if (++b) a+=b;
    c=b++;
    a*=c;
    return 0;
}
