package org.codehaus.jackson.impl;

import java.io.IOException;
import java.io.InputStream;
import java.lang.reflect.Method;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Map;

import org.codehaus.jackson.JsonGenerator;
import org.codehaus.jackson.JsonParseException;
import org.codehaus.jackson.JsonParser;
import org.codehaus.jackson.JsonProcessingException;
import org.codehaus.jackson.JsonToken;
import org.codehaus.jackson.map.DeserializationConfig;
import org.codehaus.jackson.map.DeserializationContext;
import org.codehaus.jackson.map.JsonDeserializer;
import org.codehaus.jackson.map.JsonMappingException;
import org.codehaus.jackson.map.JsonSerializer;
import org.codehaus.jackson.map.ObjectMapper;
import org.codehaus.jackson.map.SerializerProvider;
import org.codehaus.jackson.map.ser.CustomSerializerFactory;
import org.codehaus.jackson.type.JavaType;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.doukids.common.logger.Logger;
import com.doukids.common.logger.LoggerFactory;
import com.doukids.common.redis.RedisService;
import com.doukids.sign.SignUtils;
import com.doukids.web.utils.JacksonUtil;


@Component
public class DateJsonObjectMapper extends ObjectMapper {
	
	@Autowired
	RedisService redisService;
	
	private static Logger LOGGER = LoggerFactory
			.getLogger(DateJsonObjectMapper.class);

	public DateJsonObjectMapper() {
		CustomSerializerFactory factory = new CustomSerializerFactory();
		factory.addGenericMapping(Date.class, new JsonSerializer<Date>() {
			@Override
			public void serialize(Date value, JsonGenerator jsonGenerator,
					SerializerProvider provider) throws IOException,
					JsonProcessingException {
				SimpleDateFormat sdf = new SimpleDateFormat(
						"yyyy-MM-dd HH:mm:ss");
				jsonGenerator.writeString(sdf.format(value));
			}
		});
		this.setSerializerFactory(factory);
	}
	
	@SuppressWarnings("unchecked")
	public <T> T readValue(InputStream src, JavaType valueType)
			throws IOException, JsonParseException, JsonMappingException {
		return (T) _readMapAndClose(_jsonFactory.createJsonParser(src),
				valueType);
	}

	protected Object _readMapAndClose(JsonParser jp, JavaType valueType)
			throws IOException, JsonParseException, JsonMappingException {
		try {
			Object result;

			org.codehaus.jackson.impl.Utf8StreamParser p = (org.codehaus.jackson.impl.Utf8StreamParser) jp;

			 
			byte[] by = p._inputBuffer;
		 
			String jsonStr = new String(by);

			JsonToken t = _initForReading(jp);
			if (t == JsonToken.VALUE_NULL) {
				// [JACKSON-643]: Ask JsonDeserializer what 'null value' to use:
				// (note: probably no need to make a copy of config for just
				// this access)
				result = _findRootDeserializer(this._deserializationConfig,
						valueType).getNullValue();
			} else if (t == JsonToken.END_ARRAY || t == JsonToken.END_OBJECT) {
				result = null;
			} else {
				DeserializationConfig cfg = copyDeserializationConfig();
				DeserializationContext ctxt = _createDeserializationContext(jp,
						cfg);
				JsonDeserializer<Object> deser = _findRootDeserializer(cfg,
						valueType);
				//if (cfg.isEnabled(DeserializationConfig.Feature.UNWRAP_ROOT_VALUE)) {
				//	result = _unwrapAndDeserialize(jp, valueType, ctxt, deser);
				//} else {
					result = deser.deserialize(jp, ctxt);
				//}
			}
			
//			LOGGER.info("---"+jsonStr);
			Map resultMap = JacksonUtil.readValue(jsonStr, Map.class);
//			String jsonMac = (String)resultMap.get("mac");
			String jsonMes = JacksonUtil.toJSon(resultMap.get("message"));
//			Map mesMap = JacksonUtil.readValue(jsonMes, Map.class);
//			String token = (String)mesMap.get("token");
//			String signKey = null;
//			if(token != null && !"".equals(token)) {
//				signKey = (String)redisService.get(token.getBytes());
//			}
//			
//			String macApk = "";
//			if(signKey != null && !"".equals(signKey)){
//				macApk = SignUtils.encode(jsonMes,signKey);
//			}
//			
//			LOGGER.info("token:"+token);
//			LOGGER.info("signKey:"+signKey);
//			LOGGER.info("jsonMes:"+jsonMes);
//			LOGGER.info("macApk:"+macApk);
//			LOGGER.info("jsonMac:"+jsonMac);
//			
//			if(macApk.equalsIgnoreCase(jsonMac)){
//			try {
//					Method method = result.getClass().getMethod("setVail", Boolean.class);
//					method.invoke(result, true);
//				} catch (Exception e) {
//					// TODO Auto-generated catch block
//					e.printStackTrace();
//				} 
//		
//			}
			
			
//			try {
//				Method method = result.getClass().getMethod("setVail", Boolean.class);
//				method.invoke(result, true);
//			} catch (Exception e) {
//				// TODO Auto-generated catch block
//				e.printStackTrace();
//			} 
			jp.clearCurrentToken();
			return result;
		} finally {
			try {
				jp.close();
			} catch (IOException ioe) {
			}
		}
	}

}
