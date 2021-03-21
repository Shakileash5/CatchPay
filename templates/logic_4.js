var api_url = "http://127.0.0.1:5000";
function changeServer(server){
  if (server==0){
    api_url ="http://127.0.0.1:5000"
  }
  else if(server==1){
    api_url ="http://127.0.0.1:8000"
  }
}
function ajaxCall(apiurl,title,id,title_id,state=0){
    $.ajax({
    url: apiurl, 
    type:"GET",
    error: function(data){
      console.log("Server Error" , data);
      console.log(data.getAllResponseHeaders());
    },
    success: function(data){
      if(state==0)
      {
        console.log(data,id);
        document.getElementById(title_id).innerHTML = title;
        document.getElementById(id).innerHTML = data['result'];
      }
      else{
        console.log(id)
        document.getElementById(title_id).innerHTML = title;
        document.getElementById(id).style.display = "block";
        document.getElementById(id).src = data['result'];
      }
    }
  });
}

function register(){
  var uname = document.getElementById('uname').value;
  var mail = document.getElementById('mail').value;
  var password = document.getElementById('password').value;
  var url = api_url+"/register?uname="+uname+'&mail='+mail+"&password="+password;
  ajaxCall(url,"Register","res_1","title_1");
}

function ChangeButton(){
  var uname = document.getElementById('uname1').value;
  var mail = document.getElementById('mail1').value;
  var password = document.getElementById('password1').value;
  var url = api_url+"/send_otp?uname="+uname+'&mail='+mail+"&password="+password;
  ajaxCall(url,"changePassword","res_2","title_2");
}

function otpButton(){
  var otp = document.getElementById('otp').value;
  var url = api_url+"/changePassword?otp="+otp;
  ajaxCall(url,"changePassword","res_3","title_3");
}
