package com.doukids.web.controller.interceptor;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.handler.HandlerInterceptorAdapter;

import com.doukids.common.logger.Logger;
import com.doukids.common.logger.LoggerFactory;

public class LogInterceptor extends HandlerInterceptorAdapter{

	private static Logger logger = LoggerFactory.getLogger(LogInterceptor.class);
	
	@Override  
    public boolean preHandle(HttpServletRequest request,  
            HttpServletResponse response, Object handler) throws Exception {  
        // TODO Auto-generated method stub 
		logger.setGlobalId(null);
        return true;  
    } 
	
	/**
	 * This implementation is empty.
	 */
	public void postHandle(
			HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView)
			throws Exception {
		logger.setGlobalId(null);
	}

	/**
	 * This implementation is empty.
	 */
	public void afterCompletion(
			HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex)
			throws Exception {
		logger.setGlobalId(null);
	}
}
