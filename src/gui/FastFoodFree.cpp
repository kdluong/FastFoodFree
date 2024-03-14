//---------------------------------------------------------------------------

#include <fmx.h>
#ifdef _WIN32
#include <tchar.h>
#endif
#pragma hdrstop
#include <System.StartUpCopy.hpp>
//---------------------------------------------------------------------------
USEFORM("HomeForm.cpp", MyHomeForm);
USEFORM("OptionsForm.cpp", MyOptionsForm);
USEFORM("PandaExpressForm.cpp", MyPandaExpressForm);
USEFORM("SuccessForm.cpp", MySuccessForm);
USEFORM("ComingSoonForm.cpp", MyComingSoonForm);
USEFORM("FailForm.cpp", MyFailForm);
//---------------------------------------------------------------------------
extern "C" int FMXmain()
{
	try
	{
		Application->Initialize();
		Application->CreateForm(__classid(TMyHomeForm), &MyHomeForm);
		Application->CreateForm(__classid(TMyOptionsForm), &MyOptionsForm);
		Application->CreateForm(__classid(TMyPandaExpressForm), &MyPandaExpressForm);
		Application->CreateForm(__classid(TMySuccessForm), &MySuccessForm);
		Application->CreateForm(__classid(TMyFailForm), &MyFailForm);
		Application->CreateForm(__classid(TMyComingSoonForm), &MyComingSoonForm);
		Application->Run();
	}
	catch (Exception &exception)
	{
		Application->ShowException(&exception);
	}
	catch (...)
	{
		try
		{
			throw Exception("");
		}
		catch (Exception &exception)
		{
			Application->ShowException(&exception);
		}
	}
	return 0;
}
//---------------------------------------------------------------------------
