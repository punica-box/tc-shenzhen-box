var projectUrl = "https://pt.iszt.cn/invoice-webfront";
var offlineUrl = "https://pt.iszt.cn/invoice-webfront/offline/";
var onlineUrl = "https://pt.iszt.cn/invoice-webfront/online/";

var version = "V1.0.1";
var sysType = "android"
/**
 * 网络请求
 * @param {Object} func_url
 * @param {Object} params
 * @param {Object} toast
 * @param {Object} onSuccess
 * @param {Object} onError
 */
function getDataByAjax(func_url, params, toast, onSuccess, onError) {
	if(toast) {
		$('#loading').show();
	}
	
	var paramStr = encoder(params);
//	console.log(func_url + "-"+ JSON.stringify(paramStr));
	
	mui.ajax(projectUrl+func_url+'.htm', {
		data: paramStr,
		dataType: 'json',
		type: 'post',
		timeout: 30000,
		headers:{'Content-Type':'application/json'},
		success: function(data) {
			console.log(JSON.stringify(data));
			if(toast) {
				$('#loading').hide();
			}
			onSuccess(data);
		},
		error: function(xhr, type, errorThrown) {
			if(toast) {
				$('#loading').hide();
			}
			onError(type);
		}
	});
}

function getUrlParam(name){  
    //构造一个含有目标参数的正则表达式对象  
    var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");  
    //匹配目标参数  
    var r = window.location.search.substr(1).match(reg);  
    //返回参数值  verifyCode
    if (r!=null) return unescape(r[2]);  
    return null;  
}

function isHasParams(name){  
	if(window.localStorage.getItem(name)){
		return true;
	}else{
		return false;
	}
}

function getParam(name){  
    return window.localStorage.getItem(name);  
}

function saveParam(name,value){  
	return window.localStorage.setItem(name,value);  
}

function removeParam(name){
	return window.localStorage.removeItem(name);
}

function MQQBrowserCheck() {
	var iosExp = new RegExp('mqqbrowser');//ios正则
	var ua = navigator.userAgent.toLowerCase();//获取判断用的对象
	if(Terminal.platform.iPhone && iosExp.test(ua)) {
		return false;
	} else{
		return true;
	}
}

// 获取终端的相关信息
var Terminal = {
	// 辨别移动终端类型
	platform: function() {
		var u = navigator.userAgent,
			app = navigator.appVersion;
		return {
			// android终端或者uc浏览器
			android: u.indexOf('Android') > -1 || u.indexOf('Linux') > -1,
			// 是否为iPhone或者QQHD浏览器
			iPhone: u.indexOf('iPhone') > -1,
			// 是否iPad
			iPad: u.indexOf('iPad') > -1
		};
	}(),
	// 辨别移动终端的语言：zh-cn、en-us、ko-kr、ja-jp...
	language: (navigator.browserLanguage || navigator.language).toLowerCase()
}

