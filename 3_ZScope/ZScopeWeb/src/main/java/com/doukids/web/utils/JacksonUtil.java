package com.doukids.web.utils;

import java.lang.reflect.AnnotatedElement;
import java.text.SimpleDateFormat;

import org.codehaus.jackson.map.ObjectMapper;
import org.codehaus.jackson.map.introspect.Annotated;
import org.codehaus.jackson.map.introspect.AnnotatedMethod;
import org.codehaus.jackson.map.introspect.JacksonAnnotationIntrospector;
import org.springframework.format.annotation.DateTimeFormat;

/**
 * The class JacksonUtil
 *
 * json字符与对像转换
 * 
 * @version: $Revision$ $Date$ $LastChangedBy$
 *
 */
public final class JacksonUtil {
	private static final String DEFAULT_DATE_FORMAT = "yyyy-MM-dd HH:mm:ss";
	public static ObjectMapper objectMapper;
	static {

		SimpleDateFormat dateFormat = new SimpleDateFormat(DEFAULT_DATE_FORMAT);

		objectMapper = new ObjectMapper();
		objectMapper.setDateFormat(dateFormat);
		objectMapper
				.setAnnotationIntrospector(new JacksonAnnotationIntrospector() {
					@Override
					public Object findSerializer(Annotated a) {
						if (a instanceof AnnotatedMethod) {
							AnnotatedElement m = a.getAnnotated();
							DateTimeFormat an = m
									.getAnnotation(DateTimeFormat.class);
							if (an != null) {
								if (!DEFAULT_DATE_FORMAT.equals(an.pattern())) {
									return new JsonDateSerializer();
								}
							}
						}
						return super.findSerializer(a);
					}
				});
	}

	/**
	 * 使用泛型方法，把json字符串转换为相应的JavaBean对象。
	 * (1)转换为普通JavaBean：readValue(json,Student.class)
	 * (2)转换为List,如List<Student>,将第二个参数传递为Student
	 * [].class.然后使用Arrays.asList();方法把得到的数组转换为特定类型的List
	 * 
	 * @param jsonStr
	 * @param valueType
	 * @return
	 */
	public static <T> T readValue(String jsonStr, Class<T> valueType) {
		if (objectMapper == null) {
			objectMapper = new ObjectMapper();
		}

		try {
			return objectMapper.readValue(jsonStr, valueType);
		} catch (Exception e) {
			e.printStackTrace();
		}

		return null;
	}

	/**
	 * 把JavaBean转换为json字符串
	 * 
	 * @param object
	 * @return
	 */
	public static String toJSon(Object object) {
		if (objectMapper == null) {
			objectMapper = new ObjectMapper();
		}

		try {
			return objectMapper.writeValueAsString(object);
		} catch (Exception e) {
			e.printStackTrace();
		}

		return null;
	}
	public static void main(String[] args) {
		//File file = new File("")
	}

}