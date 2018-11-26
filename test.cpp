#include iostream
using namespace std;
#include <Windows.h>
#include <Iphlpapi.h>
#include <stdio.h>
#include <SetupAPI.h>
#include <devguid.h>
#include <WinBase.h>
#include <string.h>
#include <NtDDNdis.h>

#pragma comment ( lib, "Iphlpapi.lib" )
#pragma comment ( lib, "SetupAPI.lib")

void main(void){
	cout<<"test";
}

void Get_MAC_By_SETUPAPI(void) {

    HDEVINFO hardwareDeviceInfo = INVALID_HANDLE_VALUE;
    SP_DEVINFO_DATA m_devinfo_data;
    DWORD pci_dev_index_array[16] = { 0 };
    DWORD pci_dev_count = 0;
    RtlZeroMemory(&m_devinfo_data, sizeof(SP_DEVINFO_DATA));
    m_devinfo_data.cbSize = sizeof(SP_DEVINFO_DATA);

    hardwareDeviceInfo = SetupDiGetClassDevs(&GUID_DEVINTERFACE_NET, NULL, NULL, DIGCF_INTERFACEDEVICE );
    for ( DWORD i = 0; SetupDiEnumDeviceInfo(hardwareDeviceInfo, i, &m_devinfo_data) ; i++) {
        DWORD Data_Type;
        TCHAR buffer[512] = {0};
        DWORD buffersize = 512;
        DWORD req_bufsize = 0;
     
        
        wprintf_s(L"test!\n");
        while (!SetupDiGetDeviceRegistryProperty(hardwareDeviceInfo, &m_devinfo_data, SPDRP_ENUMERATOR_NAME, &Data_Type, (LPBYTE)buffer, buffersize, &req_bufsize)) {
            if (GetLastError() != ERROR_INSUFFICIENT_BUFFER)
            {
               wprintf_s(L"%s", buffer);
            }        
            else {
                wprintf_s(L"Buffer size is insufficient.\n");
            }
        }
        wprintf_s(L"Enumator index: %d: %s\n", i, buffer );
        if (!_wcsnicmp(buffer, L"PCI", 3))  // compare strings without case sensitivity.
        {
            DWORD devIndex = 0;
            SP_DEVICE_INTERFACE_DATA DevIntData;
            memset(&DevIntData, 0, sizeof(SP_DEVICE_INTERFACE_DATA));
            DevIntData.cbSize = sizeof(SP_DEVICE_INTERFACE_DATA);
            wprintf_s(L"Get PCI device\n");
            pci_dev_index_array[pci_dev_count] = i;
            pci_dev_count++;
           
            while ( SetupDiEnumDeviceInterfaces(hardwareDeviceInfo, &m_devinfo_data, &GUID_DEVINTERFACE_NET, devIndex, &DevIntData) ) {
                DWORD req_size;
                PSP_DEVICE_INTERFACE_DETAIL_DATA interface_data_buffer;
                /*  Comment this SetupDiGetDeviceInterfaceDetail. It would cause next SetupDiGetDeviceInterfaceDetail fail.
                SetupDiGetDeviceInterfaceDetail(hardwareDeviceInfo, &DevIntData, NULL, 0, &req_size, &m_devinfo_data); // get req_size 
                */
                interface_data_buffer = (PSP_DEVICE_INTERFACE_DETAIL_DATA)malloc(512); 
                ZeroMemory(interface_data_buffer, sizeof(SP_DEVICE_INTERFACE_DETAIL_DATA));
                interface_data_buffer->cbSize = sizeof(SP_DEVICE_INTERFACE_DETAIL_DATA);

                SetupDiGetDeviceInterfaceDetail(hardwareDeviceInfo, &DevIntData, interface_data_buffer, 512, &req_bufsize, &m_devinfo_data);
                wprintf_s(L"%s\n",interface_data_buffer->DevicePath);

                HANDLE handle_dev = CreateFile(interface_data_buffer->DevicePath, GENERIC_READ | GENERIC_WRITE, 0, NULL, OPEN_EXISTING, 0, 0);
                DWORD oid = OID_802_3_PERMANENT_ADDRESS;
                BYTE MACaddress[6];
                DWORD lpBytesReturned;
                if (DeviceIoControl(handle_dev, IOCTL_NDIS_QUERY_GLOBAL_STATS, &oid, sizeof(oid), MACaddress, 6, &lpBytesReturned, NULL)) {
                    DWORD err = GetLastError();
                    wprintf_s(L"%02X:%02X:%02X:%02X:%02X:%02X\n",MACaddress[0], MACaddress[1], MACaddress[2], MACaddress[3], MACaddress[4], MACaddress[5]);
                }
                devIndex++;
            }
        }        
    }

}