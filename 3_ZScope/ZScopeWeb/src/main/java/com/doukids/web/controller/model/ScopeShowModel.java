package com.doukids.web.controller.model;

public class ScopeShowModel {
	
	private String scopePubAddress;
	
	private String scopeVedioUrl;
	
	private String passPwd;
	
	public String getScopePubAddress() {
		return scopePubAddress;
	}
	
	public void setScopePubAddress(String scopePubAddress) {
		this.scopePubAddress = scopePubAddress;
	}
	
	public String getScopeVedioUrl() {
		return scopeVedioUrl;
	}
	
	public void setScopeVedioUrl(String scopeVedioUrl) {
		this.scopeVedioUrl = scopeVedioUrl;
	}

	public String getPassPwd() {
		return passPwd;
	}

	public void setPassPwd(String passPwd) {
		this.passPwd = passPwd;
	}

	@Override
	public String toString() {
		return "ScopeShowModel [scopePubAddress=" + scopePubAddress
				+ ", scopeVedioUrl=" + scopeVedioUrl + ", passPwd=" + passPwd
				+ "]";
	}

	
}
