package com.doukids.web.controller.interceptor;

import javax.servlet.ServletInputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.handler.HandlerInterceptorAdapter;

import com.doukids.common.logger.Logger;
import com.doukids.common.logger.LoggerFactory;
import com.doukids.services.common.JsonMessage;
import com.doukids.web.utils.ResponseUtils;

/**
 * 权限验证
 * 
 * @author alan.luo
 *
 */
public class PermissionsInterceptor extends HandlerInterceptorAdapter {

	private String allowUrls;

	private static Logger LOGGER = LoggerFactory
			.getLogger(PermissionsInterceptor.class);


	@SuppressWarnings({ "unchecked" })
	public boolean preHandle(HttpServletRequest request,  
            HttpServletResponse response, Object handler) throws Exception {
			ServletInputStream inputStream  = null;
			StringBuffer sb = new StringBuffer();
//			RequestObjNew requestObj = new RequestObjNew();
			try{
				System.out.println("12111111");
				/*if(handler instanceof HandlerMethod){
					HandlerMethod handlerMethod = (HandlerMethod)handler;
					MethodParameter[]methodParameters=handlerMethod.getMethodParameters();
					for (MethodParameter methodParameter : methodParameters) {
						System.out.println(methodParameter.getParameterName());
					}
				}*/
				/*inputStream =  request.getInputStream();
				byte[] by = new byte[1024];
				int length = 0;
				while((length =inputStream.read(by))!=-1){
					sb.append(new String(Arrays.copyOf(by,length)));
				}
				Map<String,String> map = JacksonUtil.readValue(sb.toString(), Map.class);
				requestObj.getMessage().setMobile(map.get("mobile"));
				requestObj.getMessage().setToken(map.get("token"));
				JsonMessage jsonMessage = checkDataUtils.checkLogin(requestObj);
				if(ResponseUtils.FAIL.equals(jsonMessage.getStatus())){
					 ResponseUtils.writeObjectToJson(response,jsonMessage);
					 return false;
				}*/
			}catch (Exception e){
				JsonMessage jsonMessage = new JsonMessage();
				jsonMessage.setStatus(ResponseUtils.FAIL);
				jsonMessage.setMessage("报文解析失败");
				ResponseUtils.writeObjectToJson(response, jsonMessage);
				LOGGER.error("报文解析失败 ",e);
			}finally{
				//inputStream.close();
			}
			
			return true;
			
	 
	}

	public String getAllowUrls() {
		return allowUrls;
	}

	public void setAllowUrls(String allowUrls) {
		this.allowUrls = allowUrls;
	}

}
