package com.doukids.web.controller;

import java.util.HashMap;
import java.util.Map;

import javax.servlet.http.HttpServletResponse;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.doukids.common.logger.Logger;
import com.doukids.common.logger.LoggerFactory;
import com.doukids.services.common.JsonMessage;
import com.doukids.web.controller.model.ScopeShowModel;
import com.github.ontio.OntSdk;
import com.github.ontio.account.Account;
import com.github.ontio.common.Helper;
import com.github.ontio.smartcontract.neovm.abi.AbiFunction;
import com.github.ontio.smartcontract.neovm.abi.AbiInfo;

@Controller
public class MicroScopeShowController{
	 
	private static Logger LOGGER = LoggerFactory.getLogger(MicroScopeShowController.class);
	
	public static String abi ="{\"hash\":\"0x58dbaa81c9be339bba11c4e2de5b57f7b24c55a0\",\"entrypoint\":\"Main\",\"functions\":[{\"name\":\"Main\",\"parameters\":[{\"name\":\"operation\",\"type\":\"String\"},{\"name\":\"args\",\"type\":\"Array\"}],\"returntype\":\"ByteArray\"},{\"name\":\"PutScope\",\"parameters\":[{\"name\":\"key\",\"type\":\"ByteArray\"},{\"name\":\"value\",\"type\":\"ByteArray\"}],\"returntype\":\"Boolean\"},{\"name\":\"GetScope\",\"parameters\":[{\"name\":\"key\",\"type\":\"ByteArray\"}],\"returntype\":\"ByteArray\"}],\"events\":[{\"name\":\"putRecord\",\"parameters\":[{\"name\":\"operation\",\"type\":\"String\"},{\"name\":\"key\",\"type\":\"ByteArray\"},{\"name\":\"value\",\"type\":\"ByteArray\"}],\"returntype\":\"Void\"},{\"name\":\"getRecord\",\"parameters\":[{\"name\":\"operation\",\"type\":\"String\"},{\"name\":\"key\",\"type\":\"ByteArray\"}],\"returntype\":\"Void\"}]}";
	
	/**
	 * 根据公共地址获取对应显微镜直播地址
	 * @param address
	 * @return
	 */
	@RequestMapping(value="/getScope",method=RequestMethod.POST)
	public @ResponseBody JsonMessage getScope(@RequestBody ScopeShowModel scopeShowModel,HttpServletResponse response) {
		
		JsonMessage jsonMessage = new JsonMessage();
		
		LOGGER.info("getScope Begin, the scopeShowModel is:" + scopeShowModel.toString());
		try{
		    //get the smart contract
			OntSdk ontSdk = getOntSdk();
			String passPwd = scopeShowModel.getPassPwd();
			String scopePubAddress = scopeShowModel.getScopePubAddress();
            byte[] key = Account.getPrivateKeyFromWIF(passPwd);

            //get the account info
            Account acct = new Account(key, ontSdk.defaultSignScheme);

            if(true){
                AbiInfo abiinfo = JSON.parseObject(abi, AbiInfo.class);
                String name = "GetScope";
                AbiFunction func = abiinfo.getFunction(name);
                func.name = name;
                System.out.println(func);
                func.setParamsValue(scopePubAddress.getBytes());

                Object obj =  ontSdk.neovm().sendTransaction(Helper.reverse("58dbaa81c9be339bba11c4e2de5b57f7b24c55a0"),acct,acct,20000,500,func, true);
                System.out.println("::::::::::::::::::::::::::::"+obj);
                String url = new String(Helper.hexToBytes(((JSONObject)obj).getString("Result")));
                jsonMessage.setStatus("1");
                jsonMessage.setData(url);
            }

		}catch(Exception e){
			jsonMessage.setStatus("0");
			LOGGER.error("getScope error, the scopeShowModel is:" + scopeShowModel.toString(),e);
			jsonMessage.setStatus("0");
			jsonMessage.setMessage("系统异常");
		}
		return jsonMessage;
	}
	
	/**
	 * 上传显微镜直播地址
	 * @param address
	 * @return
	 */
	@RequestMapping(value="/putScope",method=RequestMethod.POST)
	public @ResponseBody JsonMessage putScope(@RequestBody ScopeShowModel scopeShowModel) {
		
		JsonMessage jsonMessage = new JsonMessage();
		
		LOGGER.info("putScope Begin, the scopeShowModel is:" + scopeShowModel.toString());
		try{
		//TODO get the smart contract
			//get the smart contract
			OntSdk ontSdk = getOntSdk();
			String passPwd = scopeShowModel.getPassPwd();
			String scopePubAddress = scopeShowModel.getScopePubAddress();
			String scopeVedioUrl = scopeShowModel.getScopeVedioUrl();
            byte[] key = Account.getPrivateKeyFromWIF(passPwd);

            //get the account info
            Account acct = new Account(key, ontSdk.defaultSignScheme);

            if(true){
                AbiInfo abiinfo = JSON.parseObject(abi, AbiInfo.class);
                String name = "PutScope";
                AbiFunction func = abiinfo.getFunction(name);
                func.name = name;
                System.out.println(func);
                func.setParamsValue(scopePubAddress.getBytes());
                func.setParamsValue(scopeVedioUrl.getBytes());

                Object obj =  ontSdk.neovm().sendTransaction(Helper.reverse("58dbaa81c9be339bba11c4e2de5b57f7b24c55a0"),acct,acct,20000,500,func, false);
                System.out.println(obj);
                jsonMessage.setStatus("1");
                Map resultMap = new HashMap();
                resultMap.put("showUrl", "");
                
                jsonMessage.setData(resultMap);
                
                return jsonMessage;
            }	
			
			
			
			
			
			
		}catch(Exception e){
			jsonMessage.setStatus("0");
			LOGGER.error("putScope error, the address is:" + scopeShowModel,e);
			jsonMessage.setStatus("0");
			jsonMessage.setMessage("系统异常");
		}
	
		return jsonMessage;
	}
	
	public static OntSdk getOntSdk() throws Exception {

      String ip = "http://polaris1.ont.io";
      String restUrl = ip + ":" + "20334";
      String rpcUrl = ip + ":" + "20336";
      String wsUrl = ip + ":" + "20335";

      OntSdk wm = OntSdk.getInstance();
      wm.setRpc(rpcUrl);
      wm.setRestful(restUrl);
      wm.setDefaultConnect(wm.getRestful());
      wm.openWalletFile("nep5.json");
      return wm;
  }
}
