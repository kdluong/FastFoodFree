//---------------------------------------------------------------------------

#include <fmx.h>
#include <System.SysUtils.hpp>
#pragma hdrstop

#include "PandaExpressForm.h"
#include "OptionsForm.h"
#include "SuccessForm.h"
#include "FailForm.h"
#include <cctype>
#include <regex>
#include <memory>

#include <vcl.h>
#include <System.Net.HttpClient.hpp>
#include <System.Classes.hpp>
#include <System.JSON.hpp>

//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.fmx"
TMyPandaExpressForm *MyPandaExpressForm;
//---------------------------------------------------------------------------
__fastcall TMyPandaExpressForm::TMyPandaExpressForm(TComponent* Owner)
	: TForm(Owner)
{
    RESTRequest1->OnAfterExecute = RESTRequest1AfterExecute;
}
//---------------------------------------------------------------------------
void __fastcall TMyPandaExpressForm::BackButtonClick(TObject *Sender)
{
	this->Close();
}
//---------------------------------------------------------------------------
bool TMyPandaExpressForm::ValidCode(std::string value, int maxLength)
{
	if (value.length() == maxLength)
	{
		for(int i = 0; i < maxLength; i++)
		{
			if(!isdigit(value[i]))
			{
				return false;
			}
		}

		return true;
	}

	return false;
}
bool TMyPandaExpressForm::ValidEmail(std::string email)
{
	const std::regex pattern(R"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})");
	return std::regex_match(email, pattern);
}
//---------------------------------------------------------------------------
void __fastcall TMyPandaExpressForm::RESTRequest1AfterExecute(TCustomRESTRequest *Sender)
{
	bool successFlag = false;
	std::string message = "";

	TJSONObject *JsonResponse = (TJSONObject*)TJSONObject::ParseJSONValue(RESTResponse1->Content);

	if(JsonResponse)
	{
		if(JsonResponse->GetValue("statusCode")->Value() == 200)
		{
			successFlag = true;
		}
	}
	else
	{
		message = "We've encountered an error. Please try again.";
	}

	if(successFlag)
	{
		Code1Edit->Text = "";
		Code2Edit->Text = "";
		Code3Edit->Text = "";
		Code4Edit->Text = "";
		Code5Edit->Text = "";
		Code6Edit->Text = "";
		EmailEdit->Text = "";

		this->Close();

		std::unique_ptr<TMySuccessForm> successForm(new TMySuccessForm(NULL));
		successForm->ShowModal();
	}
	else
	{
		std::unique_ptr<TMyFailForm> failForm(new TMyFailForm(NULL));

		if(message == "")
		{
			failForm->Label1->Text = JsonResponse->GetValue("body")->Value();
		}
		else
		{
			failForm->Label1->Text = System::UnicodeString(message.c_str());
		}

		failForm->ShowModal();
	}

	ToggleEnabled();
}
//---------------------------------------------------------------------------
void __fastcall TMyPandaExpressForm::SubmitButtonClick(TObject *Sender)
{
	ToggleEnabled();
	std::string message = "";
	bool failFlag = false;

	std::string code1 = AnsiString(Code1Edit->Text).c_str();
	std::string code2 = AnsiString(Code2Edit->Text).c_str();
	std::string code3 = AnsiString(Code3Edit->Text).c_str();
	std::string code4 = AnsiString(Code4Edit->Text).c_str();
	std::string code5 = AnsiString(Code5Edit->Text).c_str();
	std::string code6 = AnsiString(Code6Edit->Text).c_str();
	std::string email = AnsiString(EmailEdit->Text).c_str();

	// Check for valid inputs

	if(	!ValidCode(code1, 4) ||
		!ValidCode(code2, 4) ||
		!ValidCode(code3, 4) ||
		!ValidCode(code4, 4) ||
		!ValidCode(code5, 4) ||
		!ValidCode(code6, 2)	)
	{
		message = "Invalid Survey Code.";
		failFlag = true;
	}
	else if( !ValidEmail(email) )
	{
		message = "Invalid Email Address.";
		failFlag = true;
	}

	// Connect w/ Google Cloud

	if(!failFlag)
	{
		// Get visit type

		int visitType = 0;

		if(DeliveryButton->IsChecked)
		{
			visitType = 1;
		}
		else if(PickUpButton->IsChecked)
		{
			visitType = 2;
		}

		// Get rating

		int rating = 5;

		if(Rating1Button->IsChecked)
		{
			rating = 1;
		}
		else if(Rating2Button->IsChecked)
		{
			rating = 2;
		}
		else if(Rating3Button->IsChecked)
		{
			rating = 3;
		}
		else if(Rating4Button->IsChecked)
		{
			rating = 4;
		}

		// Create JSON

        TJSONArray *surveyArray = new TJSONArray;

		surveyArray->Add(Code1Edit->Text);
		surveyArray->Add(Code2Edit->Text);
		surveyArray->Add(Code3Edit->Text);
		surveyArray->Add(Code4Edit->Text);
		surveyArray->Add(Code5Edit->Text);
		surveyArray->Add(Code6Edit->Text);

		TJSONObject *RequestData = new TJSONObject();

		RequestData->AddPair("option", "panda_express");
		RequestData->AddPair("survey_code", surveyArray);
		RequestData->AddPair("rating", rating);
		RequestData->AddPair("email", EmailEdit->Text);
		RequestData->AddPair("visit_type", visitType);

		UnicodeString jsonString = RequestData->ToString();

		// Call REST API (POST)

		RESTClient1->BaseURL = L"https://us-west2-sincere-woods-416422.cloudfunctions.net";
		RESTRequest1->Resource = L"/function-1"; // Endpoint path
		RESTRequest1->AddBody(RequestData);

		RESTRequest1->Execute();
	}
	else
	{
		ToggleEnabled();

        std::unique_ptr<TMyFailForm> failForm(new TMyFailForm(NULL));
		failForm->Label1->Text = System::UnicodeString(message.c_str());
		failForm->ShowModal();
	}
}
//---------------------------------------------------------------------------
void TMyPandaExpressForm::ToggleEnabled()
{
	Code1Edit->Enabled = !Code1Edit->Enabled;
	Code2Edit->Enabled = !Code2Edit->Enabled;
	Code3Edit->Enabled = !Code3Edit->Enabled;
	Code4Edit->Enabled = !Code4Edit->Enabled;
	Code5Edit->Enabled = !Code5Edit->Enabled;
	Code6Edit->Enabled = !Code6Edit->Enabled;

	EmailEdit->Enabled = !EmailEdit->Enabled;

	Rating1Button->Enabled = !Rating1Button->Enabled;
	Rating2Button->Enabled = !Rating2Button->Enabled;
	Rating3Button->Enabled = !Rating3Button->Enabled;
	Rating4Button->Enabled = !Rating4Button->Enabled;
	Rating5Button->Enabled = !Rating5Button->Enabled;

	DineInButton->Enabled = !DineInButton->Enabled;
	PickUpButton->Enabled = !PickUpButton->Enabled;
	DeliveryButton->Enabled = !DeliveryButton->Enabled;

	SubmitButton->Enabled = !SubmitButton->Enabled;
	BackButton->Enabled = !BackButton->Enabled;
}

