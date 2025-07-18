print("select two subject : \nmath. \nprograming. \nphysics. \nAI concept. \nstatistics. \nchemistry. \nbiology. \ncircutis. ")
sub1=input("enter the first subject:")
sub2=input("enter the second subject:")
if((sub1=="math" and sub2=="programing") or (sub1=="programing"and sub2=="math")):
    print("course is: computer engineering \n ")
elif((sub1=="math" and sub2=="physics") or (sub1=="physics"and sub2=="math")):
    print("course is: mechenical engineering \n")
elif ((sub1=="AI concept"and sub2=="statistics") or (sub1=="statistics"and sub2=="AI concept")):
    print("course is: artifical engineering \n")
elif ((sub1=="chemistry"and sub2=="biology") or (sub1=="biology"and sub2=="chemistry")):
    print("course is: biotechnologycal engineering \n")
elif ((sub1=="circutis"and sub2=="math") or (sub1=="math"and sub2=="circuit ")):
    print("course is: electronics engineering \n")
