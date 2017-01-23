int lengthOfLastWord(char* s) {
    int i;
    int pos=-1;
    if (*s==0) return 0;
    for(i=0;;i++)
    {
       if (*(s+i)==0) 
       {
           break;
       }
       else if (*(s+i)==' ')
       {
           pos=i;
       }
    }
    if (pos==(i-1)) 
    {
        *(s+pos)=0;
        return lengthOfLastWord(s);
    }
    if (pos==-1)
    {
        
        return i;
    }
    return i-pos-1;
    
}
int lengthOfLastWord(char* s) {
    int i,k;
    int pos=-1;
    int boo=0;
    if (*s==0) return 0;
    
    for(i=0;;i++)
    {
       if (*(s+i)==0) 
       {
           break;
       }
       else if (*(s+i)==' ')
       {
           pos=i;
       }
    }
    if (pos==(i-1)) 
    {
        for (k=i-2;k>=0;k--)
        {
            if ((*(s+k)!=' ')&&!boo)
            {
                pos=k;
                //printf ("%d",k);
                boo=1;
            }
            if ((*(s+k)==' ')&&boo)
            {
                
                return pos-k;
            }
            if (k==0&&boo)
            {
                return pos+1;
            }
        }
        return 0;
        
    }
    if (pos==-1)
    {
        
        return i;
    }
    
    return i-pos-1;
    
}