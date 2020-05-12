BEGIN { print "START" }

{
   # get the path 
   split($0, a , ",");
   path = a[2] 
   idx = split(a[2], b, "-");
    version = a[3]
    #print path
    #print b[idx] "b[idx] " a[3] "  a[3]"
    print a[1]
    system("java -jar DesigniteJava.jar -i " "./"path " -o " "./output-final/"b[idx]"sep"a[1]"sep"a[3]"/")
    }

END { print "END" }

