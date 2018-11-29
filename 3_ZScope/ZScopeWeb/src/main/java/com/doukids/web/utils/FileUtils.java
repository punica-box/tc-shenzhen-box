package com.doukids.web.utils;

import java.awt.image.BufferedImage;
import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.util.ArrayList;
import java.util.List;

import javax.imageio.ImageIO;

import sun.misc.*;


/**
 * 文件工具类
 * 
 * @author alan.luo
 *
 */
public class FileUtils {
	/**
	 * 保存上传文件
	 * @param stream
	 * @param path
	 * @param filename
	 * @throws IOException
	 */
	public static  void SaveFileFromInputStream(InputStream stream, String path,
			String filename) throws IOException {
		File newFile = new File(path);
		if(!newFile.exists()){
			newFile.mkdirs();
		}
		FileOutputStream fs = new FileOutputStream(path + "/" + filename);
		byte[] buffer = new byte[1024 * 1024];
		int bytesum = 0;
		int byteread = 0;
		while ((byteread = stream.read(buffer)) != -1) {
			bytesum += byteread;
			fs.write(buffer, 0, byteread);
			fs.flush();
		}
		fs.close();
		stream.close();
	}
	
	/**
	 * 读取图片 已base64形式返回
	 * @param path
	 * @return
	 */
	public static String readPic(String path){
		File file = new File(path);
		ByteArrayOutputStream outputStream = null;
	    try {
	      BufferedImage bufferedImage = ImageIO.read(file);
	      outputStream = new ByteArrayOutputStream();
	      ImageIO.write(bufferedImage, "jpg", outputStream);
	    } catch (MalformedURLException e1) {
	      e1.printStackTrace();
	    } catch (IOException e) {
	      e.printStackTrace();
	    }
	    // 对字节数组Base64编码
	    BASE64Encoder encoder = new BASE64Encoder();
	    return encoder.encode(outputStream.toByteArray());// 返回Base64编码过的字节数组字符串
	}
	
	/**
	 * 按行读取TXT文件
	 * @param filepath
	 * @return
	 * @throws IOException
	 */
	public static List readFilesForInputStream(InputStream inputStream) throws IOException {  
       
        List<String> returnList = new ArrayList();
        InputStreamReader reader = new InputStreamReader(inputStream); 
        BufferedReader br = new BufferedReader(reader);
        String line = "";  
        line = br.readLine();  
        while (line != null) {  
            
            if(line != null)
            {
              returnList.add(line);
              System.out.println(line);
            }
            line = br.readLine(); // 一次读入一行数据  
        }
        
        return returnList;
    }
	
	/**
	 * 按行读取TXT文件
	 * @param filepath
	 * @return
	 * @throws IOException
	 */
	public static List readFiles(String filepath) throws IOException {  
        File filename = new File(filepath);
        
        List<String> returnList = new ArrayList();
        InputStreamReader reader = new InputStreamReader(  
                new FileInputStream(filename)); 
        BufferedReader br = new BufferedReader(reader);
        String line = "";  
        line = br.readLine();  
        while (line != null) {  
            if(line != null)
            {
              returnList.add(line);
              System.out.println(line);
            }
            line = br.readLine(); // 一次读入一行数据  
        }
        
        return returnList;
    }
	
	public static void main(String[] args)
	{
		File file = new File("D:\\My Thing\\xiaoyupay2.0\\数据迁移\\account_v17_test.txt");
		try {
			List list = readFilesForInputStream(new FileInputStream(file));
			System.out.println("~~~~~~~~~~~~~~"+list);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		System.out.println();
	}
	
}
