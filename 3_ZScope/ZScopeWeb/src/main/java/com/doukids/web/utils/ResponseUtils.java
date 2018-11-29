package com.doukids.web.utils;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.http.HttpServletResponse;

import org.apache.log4j.Logger;

/**
 * 把对象转成json数据输出
 * @author alan.luo
 *
 */
public class ResponseUtils {
	private static Logger logger = Logger.getLogger(ResponseUtils.class);
	public static String SUCCESS= "1";
	public static String FAIL = "0";
	public static String writeObjectToJson(HttpServletResponse response , Object obj){
		PrintWriter pw = null;
		try {
			response.setCharacterEncoding("UTF-8");
			pw = response.getWriter();
			String json =  JacksonUtil.toJSon(obj);
			pw.write(json);
		} catch (IOException e) {
			logger.error("-------to write json error --------",e);
		}
		finally {
			pw.close();
		}
		return null;
		
	}

}
