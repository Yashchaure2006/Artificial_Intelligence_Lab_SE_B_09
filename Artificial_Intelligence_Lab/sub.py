print("select the subject \n math. \n physics. \n chemistry. \n biology. \n programing. \n circuits. \n AI concept. \n statistics.")
sub1=input ("first subjct is ")
sub2=input ("second subject is " )

if((sub1=="math" and sub2=="physics") or (sub1=="physics" and sub2=="math")):
 		print("suggeted branch"  " machanical engineering")
elif((sub1=="math" and sub2=="programing") or (sub1=="programing" and sub2=="math")):
 		print("suggeted branch"  "computer engineering")
elif((sub1=="biology" and sub2=="chemistry") or (sub1=="chemistry" and sub2=="biology")):
 		print("suggeted branch"  "biotechnology engineering")
elif((sub1=="circuits" and sub2=="math") or (sub1=="math" and sub2=="circuits")):
 		print("suggeted branch"  "electronic engineering") 		
elif((sub1=="programing" and sub2=="statistics") or (sub1=="statistics" and sub2=="programing")):
 		print("suggeted branch"  "Artificial Intelligence engineering") 		
elif((sub1=="programing" and sub2=="AI concept") or (sub1=="AI concept" and sub2=="programing")):
 		print("suggeted branch"  "Artificial Intelligence and Machine Learning engineering") 		
