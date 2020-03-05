class Solution {
    public String longestPalindrome(String s) {
    char[] c = s.toCharArray();
	String fs = "";
	if(c.length==1){
		return s;
	}else if(c.length==2){
		if(s.charAt(0)==s.charAt(1)){
			return s;
			}else{
		return s.substring(1);
			}
	}
	else{
	for (int i = 0;i<c.length-1;i++){
		for(int j = i + 1;j < c.length;j++){
			if(c[i] == c[j]){
				int flag = 0;
				if((j-i)%2==0){
					for(int k = 0;k<(j-i)/2+1;k++){
						if(c[i+k]!=c[j-k]){
							flag++;
						}
					}
				}else{
					for(int l = 0;l<(j-i)/2+2;l++){
						if(c[i+l]!=c[j-l]){
							flag++;
						}
					}
				}
                if(flag==0){
                        if((j-i+1)>fs.length()){
                        fs = s.substring(i, j+1);
                }
            }
			}
			}
		}
	if(fs=="" && s.length()>0){
		 char ff = s.charAt(0);
         fs = String.valueOf(ff);
	}
    return fs;
    }
}
}